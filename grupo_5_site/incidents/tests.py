"""
Testes do app incidents — Detecção de Anomalias (Grupo 5)

Cobertura:
  - storage: load_history, append_analysis, clear_history, save_history
  - gemini_client: build_prompt, parse_analysis_json
  - views: GET / → 200 + template
  - views: POST / com evento válido (mock do analyze_event retorna dict)
  - views: POST / com erro no Gemini (mock levanta exceção)
  - views: POST /limpar/ → redireciona e limpa histórico
  - views: POST / sem campo event → redireciona sem criar entrada
"""

import json
import os
import tempfile
from pathlib import Path
from unittest.mock import patch

from django.test import Client, TestCase, override_settings

SAMPLE_ANALYSIS = {
    "resumo": "Sequência de 42 falhas seguida de acesso bem-sucedido.",
    "severidade": "crítica",
    "fatores": ["Muitas falhas + sucesso", "Conta privilegiada"],
    "classificacao": "incidente confirmado",
    "hipotese": "Ataque de força bruta bem-sucedido.",
    "acoes": ["Correlacionar IP", "Verificar MFA"],
    "falso_positivo": "Baixa probabilidade.",
    "decisao": "Escalar imediatamente.",
    "restricoes": "Não executar bloqueio automático.",
}


# ─── helpers ────────────────────────────────────────────────────────────────

def _tmp_json_path() -> Path:
    fd, path_str = tempfile.mkstemp(suffix=".json")
    os.close(fd)
    tmp = Path(path_str)
    tmp.write_text("[]", encoding="utf-8")
    return tmp


def _tmp_md_path(content: str = "# skill") -> Path:
    fd, path_str = tempfile.mkstemp(suffix=".md")
    os.close(fd)
    tmp = Path(path_str)
    tmp.write_text(content, encoding="utf-8")
    return tmp


# ─── Storage ─────────────────────────────────────────────────────────────────

class StorageTests(TestCase):
    def setUp(self):
        self.conversa = _tmp_json_path()
        self.skill = _tmp_md_path("# SKILL")
        self.memoria = _tmp_md_path("# MEMORIA")

    def tearDown(self):
        for p in (self.conversa, self.skill, self.memoria):
            p.unlink(missing_ok=True)

    def _settings(self):
        return override_settings(
            CONVERSA_PATH=self.conversa,
            SKILL_PATH=self.skill,
            MEMORIA_PATH=self.memoria,
        )

    def test_load_history_empty(self):
        with self._settings():
            from incidents.storage import load_history
            self.assertEqual(load_history(), [])

    def test_append_and_load(self):
        with self._settings():
            from incidents import storage
            storage.append_analysis("evento 1", SAMPLE_ANALYSIS, status="ok")
            history = storage.load_history()
            self.assertEqual(len(history), 1)
            self.assertEqual(history[0]["evento"], "evento 1")
            self.assertEqual(history[0]["status"], "ok")

    def test_append_stores_dict_analysis(self):
        with self._settings():
            from incidents import storage
            storage.append_analysis("ev", SAMPLE_ANALYSIS)
            history = storage.load_history()
            self.assertEqual(history[0]["analise"]["severidade"], "crítica")
            self.assertIsInstance(history[0]["analise"]["fatores"], list)

    def test_append_multiple(self):
        with self._settings():
            from incidents import storage
            storage.append_analysis("ev1", SAMPLE_ANALYSIS)
            storage.append_analysis("ev2", SAMPLE_ANALYSIS)
            history = storage.load_history()
            self.assertEqual(len(history), 2)
            self.assertEqual(history[1]["evento"], "ev2")

    def test_clear_history(self):
        with self._settings():
            from incidents import storage
            storage.append_analysis("ev", SAMPLE_ANALYSIS)
            storage.clear_history()
            self.assertEqual(storage.load_history(), [])

    def test_load_with_limit(self):
        with self._settings():
            from incidents import storage
            for i in range(5):
                storage.append_analysis(f"ev{i}", SAMPLE_ANALYSIS)
            limited = storage.load_history(limit=3)
            self.assertEqual(len(limited), 3)
            self.assertEqual(limited[0]["evento"], "ev2")

    def test_save_and_reload_json(self):
        with self._settings():
            from incidents import storage
            storage.append_analysis("teste", SAMPLE_ANALYSIS, status="ok")
            data = json.loads(self.conversa.read_text(encoding="utf-8"))
            self.assertIsInstance(data, list)
            self.assertEqual(data[0]["evento"], "teste")

    def test_corrupted_json_returns_empty(self):
        self.conversa.write_text("INVALIDO{{", encoding="utf-8")
        with self._settings():
            from incidents.storage import load_history
            self.assertEqual(load_history(), [])

    def test_read_text_file_missing(self):
        with self._settings():
            from incidents.storage import read_text_file
            result = read_text_file(Path("/nao/existe.md"), default="fallback")
            self.assertEqual(result, "fallback")

    def test_read_text_file_existing(self):
        with self._settings():
            from incidents.storage import read_text_file
            result = read_text_file(self.skill)
            self.assertEqual(result, "# SKILL")


# ─── Gemini Client ────────────────────────────────────────────────────────────

class GeminiClientTests(TestCase):
    def setUp(self):
        self.skill = _tmp_md_path("## Papel do assistente\nAnalisar eventos.")
        self.memoria = _tmp_md_path("## Regras\n- Contexto importa.")
        self.conversa = _tmp_json_path()

    def tearDown(self):
        for p in (self.skill, self.memoria, self.conversa):
            p.unlink(missing_ok=True)

    def _settings(self):
        return override_settings(
            SKILL_PATH=self.skill,
            MEMORIA_PATH=self.memoria,
            CONVERSA_PATH=self.conversa,
        )

    def test_build_prompt_contains_event(self):
        with self._settings():
            from incidents.gemini_client import build_prompt
            prompt = build_prompt("42 falhas de login às 03h17", [])
            self.assertIn("42 falhas de login às 03h17", prompt)

    def test_build_prompt_contains_skill(self):
        with self._settings():
            from incidents.gemini_client import build_prompt
            prompt = build_prompt("evento", [])
            self.assertIn("Analisar eventos.", prompt)

    def test_build_prompt_contains_memoria(self):
        with self._settings():
            from incidents.gemini_client import build_prompt
            prompt = build_prompt("evento", [])
            self.assertIn("Contexto importa.", prompt)

    def test_build_prompt_includes_history(self):
        with self._settings():
            from incidents.gemini_client import build_prompt
            history = [{"id": 1, "evento": "ev anterior", "analise": SAMPLE_ANALYSIS}]
            prompt = build_prompt("novo evento", history)
            self.assertIn("ev anterior", prompt)

    def test_build_prompt_missing_skill_shows_fallback(self):
        missing = Path("/nao/existe/skill.md")
        with override_settings(
            SKILL_PATH=missing,
            MEMORIA_PATH=self.memoria,
            CONVERSA_PATH=self.conversa,
        ):
            from incidents.gemini_client import build_prompt
            prompt = build_prompt("evento", [])
            self.assertIn("SKILL.md não encontrado.", prompt)

    def test_build_prompt_requests_json_output(self):
        with self._settings():
            from incidents.gemini_client import build_prompt
            prompt = build_prompt("evento", [])
            self.assertIn("JSON", prompt)

    # parse_analysis_json

    def test_parse_valid_json(self):
        from incidents.gemini_client import parse_analysis_json
        raw = json.dumps(SAMPLE_ANALYSIS)
        result = parse_analysis_json(raw)
        self.assertEqual(result["severidade"], "crítica")
        self.assertIsInstance(result["fatores"], list)

    def test_parse_json_in_markdown_block(self):
        from incidents.gemini_client import parse_analysis_json
        raw = f"```json\n{json.dumps(SAMPLE_ANALYSIS)}\n```"
        result = parse_analysis_json(raw)
        self.assertEqual(result["resumo"], SAMPLE_ANALYSIS["resumo"])

    def test_parse_json_extracts_embedded_object(self):
        from incidents.gemini_client import parse_analysis_json
        raw = f'Aqui está a análise:\n{json.dumps(SAMPLE_ANALYSIS)}\nFim.'
        result = parse_analysis_json(raw)
        self.assertEqual(result["classificacao"], SAMPLE_ANALYSIS["classificacao"])

    def test_parse_invalid_json_returns_fallback(self):
        from incidents.gemini_client import parse_analysis_json
        raw = "Texto sem JSON nenhum."
        result = parse_analysis_json(raw)
        self.assertEqual(result["resumo"], raw)
        self.assertEqual(result["fatores"], [])

    def test_parse_partial_json_fills_missing_keys(self):
        from incidents.gemini_client import parse_analysis_json
        raw = json.dumps({"resumo": "teste", "severidade": "alta"})
        result = parse_analysis_json(raw)
        self.assertEqual(result["resumo"], "teste")
        self.assertEqual(result["fatores"], [])

    def test_analyze_event_raises_without_api_key(self):
        with self._settings():
            env = {k: v for k, v in os.environ.items()
                   if k not in ("GOOGLE_API_KEY", "GEMINI_API_KEY")}
            with patch.dict(os.environ, env, clear=True):
                from incidents.gemini_client import analyze_event
                with self.assertRaises(RuntimeError) as ctx:
                    analyze_event("evento teste", [])
                self.assertIn("não configurada", str(ctx.exception))


# ─── Views ───────────────────────────────────────────────────────────────────

class ViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.conversa = _tmp_json_path()
        self.skill = _tmp_md_path("# SKILL")
        self.memoria = _tmp_md_path("# MEMORIA")

    def tearDown(self):
        for p in (self.conversa, self.skill, self.memoria):
            p.unlink(missing_ok=True)

    def _settings(self):
        return override_settings(
            CONVERSA_PATH=self.conversa,
            SKILL_PATH=self.skill,
            MEMORIA_PATH=self.memoria,
            GEMINI_MODEL="gemini/gemini-test",
            MAX_CONVERSATION_MESSAGES=12,
        )

    def test_get_index_returns_200(self):
        with self._settings():
            response = self.client.get("/")
            self.assertEqual(response.status_code, 200)

    def test_get_index_uses_correct_template(self):
        with self._settings():
            response = self.client.get("/")
            self.assertTemplateUsed(response, "incidents/index.html")

    def test_get_index_context_has_history_and_model(self):
        with self._settings():
            response = self.client.get("/")
            self.assertIn("history", response.context)
            self.assertIn("model_name", response.context)
            self.assertEqual(response.context["model_name"], "gemini/gemini-test")

    def test_get_index_history_empty_initially(self):
        with self._settings():
            response = self.client.get("/")
            self.assertEqual(response.context["history"], [])

    @patch("incidents.views.analyze_event", return_value=SAMPLE_ANALYSIS)
    def test_post_valid_event_redirects(self, mock_analyze):
        with self._settings():
            response = self.client.post("/", {"event": "42 falhas de login"})
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, "/")

    @patch("incidents.views.analyze_event", return_value=SAMPLE_ANALYSIS)
    def test_post_valid_event_saves_dict_to_history(self, mock_analyze):
        with self._settings():
            self.client.post("/", {"event": "42 falhas de login"})
            response = self.client.get("/")
            history = response.context["history"]
            self.assertEqual(len(history), 1)
            self.assertEqual(history[0]["evento"], "42 falhas de login")
            self.assertEqual(history[0]["analise"]["severidade"], "crítica")
            self.assertEqual(history[0]["status"], "ok")

    @patch("incidents.views.analyze_event", side_effect=RuntimeError("API offline"))
    def test_post_gemini_error_saves_error_entry(self, mock_analyze):
        with self._settings():
            self.client.post("/", {"event": "evento teste"})
            response = self.client.get("/")
            history = response.context["history"]
            self.assertEqual(history[0]["status"], "erro")
            self.assertIn("API offline", history[0]["analise"]["resumo"])

    def test_post_empty_event_does_not_create_history(self):
        with self._settings():
            self.client.post("/", {"event": "   "})
            response = self.client.get("/")
            self.assertEqual(response.context["history"], [])

    def test_post_missing_event_field_does_not_create_history(self):
        with self._settings():
            self.client.post("/", {})
            response = self.client.get("/")
            self.assertEqual(response.context["history"], [])

    def test_post_clear_redirects(self):
        with self._settings():
            response = self.client.post("/limpar/")
            self.assertEqual(response.status_code, 302)

    @patch("incidents.views.analyze_event", return_value=SAMPLE_ANALYSIS)
    def test_post_clear_removes_all_history(self, mock_analyze):
        with self._settings():
            self.client.post("/", {"event": "ev1"})
            self.client.post("/", {"event": "ev2"})
            self.client.post("/limpar/")
            response = self.client.get("/")
            self.assertEqual(response.context["history"], [])

    @patch("incidents.views.analyze_event", return_value=SAMPLE_ANALYSIS)
    def test_multiple_events_accumulate(self, mock_analyze):
        with self._settings():
            self.client.post("/", {"event": "ev1"})
            self.client.post("/", {"event": "ev2"})
            response = self.client.get("/")
            self.assertEqual(len(response.context["history"]), 2)

    def test_get_only_view_rejects_post_on_clear_with_wrong_method(self):
        with self._settings():
            response = self.client.get("/limpar/")
            self.assertEqual(response.status_code, 405)
