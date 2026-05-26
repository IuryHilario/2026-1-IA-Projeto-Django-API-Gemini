from __future__ import annotations

from datetime import datetime, timezone
import json
import os
from pathlib import Path
from typing import Any

from django.conf import settings


def read_text_file(path: Path, default: str = "") -> str:
    if not path.exists():
        return default
    return path.read_text(encoding="utf-8").strip()


def load_conversation(limit: int | None = None) -> list[dict[str, Any]]:
    path = settings.CONVERSA_PATH
    if not path.exists():
        save_conversation([])
        return []

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

    if not isinstance(data, list):
        return []

    messages = [item for item in data if isinstance(item, dict)]
    if limit is None:
        return messages
    return messages[-limit:]


def save_conversation(messages: list[dict[str, Any]]) -> None:
    path = settings.CONVERSA_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_suffix(".json.tmp")
    tmp_path.write_text(
        json.dumps(messages, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    os.replace(tmp_path, path)


def append_turn(question: str, answer: str, status: str = "ok") -> list[dict[str, Any]]:
    messages = load_conversation()
    messages.append(
        {
            "id": len(messages) + 1,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "pergunta": question,
            "resposta": answer,
            "status": status,
        }
    )
    save_conversation(messages)
    return messages


def clear_conversation() -> None:
    save_conversation([])
