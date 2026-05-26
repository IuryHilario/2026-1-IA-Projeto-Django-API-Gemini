from django.conf import settings
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .crew_client import ask_gemini_with_crewai
from .storage import append_turn, clear_conversation, load_conversation


@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == "POST":
        question = request.POST.get("message", "").strip()
        if question:
            history = load_conversation(limit=settings.MAX_CONVERSATION_MESSAGES)
            try:
                answer = ask_gemini_with_crewai(question, history)
                append_turn(question, answer, status="ok")
            except Exception as exc:
                answer = (
                    "Não foi possível obter resposta do Gemini via CrewAI.\n\n"
                    f"Detalhe técnico: {exc}"
                )
                append_turn(question, answer, status="erro")
        return redirect("chat_index")

    return render(
        request,
        "chat/index.html",
        {
            "conversation": load_conversation(),
            "model_name": settings.GEMINI_MODEL,
        },
    )


@require_http_methods(["POST"])
def clear_history(request):
    clear_conversation()
    return redirect("chat_index")
