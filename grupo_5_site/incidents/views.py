from django.conf import settings
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .gemini_client import analyze_event
from .storage import append_analysis, clear_history, load_history


@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == "POST":
        event = request.POST.get("event", "").strip()
        if event:
            history = load_history(limit=settings.MAX_CONVERSATION_MESSAGES)
            try:
                analysis = analyze_event(event, history)
                append_analysis(event, analysis, status="ok")
            except Exception as exc:
                analysis = {"resumo": f"Erro ao obter análise: {exc}"}
                append_analysis(event, analysis, status="erro")
        return redirect("incidents_index")

    return render(
        request,
        "incidents/index.html",
        {
            "history": load_history(),
            "model_name": settings.GEMINI_MODEL,
        },
    )


@require_http_methods(["POST"])
def clear(request):
    clear_history()
    return redirect("incidents_index")
