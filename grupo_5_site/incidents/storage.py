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


def load_history(limit: int | None = None) -> list[dict[str, Any]]:
    path = settings.CONVERSA_PATH
    if not path.exists():
        save_history([])
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


def save_history(messages: list[dict[str, Any]]) -> None:
    path = settings.CONVERSA_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(messages, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(tmp, path)


def append_analysis(event: str, analysis: str, status: str = "ok") -> None:
    messages = load_history()
    messages.append(
        {
            "id": len(messages) + 1,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "evento": event,
            "analise": analysis,
            "status": status,
        }
    )
    save_history(messages)


def clear_history() -> None:
    save_history([])
