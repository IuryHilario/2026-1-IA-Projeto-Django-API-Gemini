# Django Exemplo: Chat com CrewAI + Gemini

Projeto simples para demonstrar uma página de chat que envia ao modelo:

- a pergunta do usuário;
- o arquivo `SKILL.md`;
- o arquivo `memoria.md`;
- o histórico salvo em `conversa.json`.

O histórico da conversa é gravado em `conversa.json` na raiz desta pasta.

## Como rodar

```bash
cd django_exemplo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Edite o arquivo `.env` e coloque sua chave do Google em `GOOGLE_API_KEY`.

Depois rode:

```bash
python manage.py runserver
```

Acesse:

```text
http://127.0.0.1:8000/
```

## Arquivos principais

- `SKILL.md`: instruções de comportamento do assistente.
- `memoria.md`: memória simulada do sistema em produção.
- `conversa.json`: histórico persistido da conversa.
- `chat/crew_client.py`: monta o prompt e chama CrewAI/Gemini.
- `chat/storage.py`: lê e grava arquivos locais.
- `chat/views.py`: controla a tela de chat.

## Trocar a skill

Para usar outro grupo da atividade, substitua o conteúdo de `SKILL.md` e `memoria.md` pelos arquivos do grupo desejado. O código não precisa ser alterado.

## Observações

- O exemplo foi feito para aula e desenvolvimento local.
- Não coloque chave de API real em repositórios públicos.
- O modelo padrão é `gemini/gemini-2.5-flash-lite`, mas pode ser alterado em `GEMINI_MODEL`.
- O projeto mantém apenas um arquivo JSON local; não usa banco de dados.
