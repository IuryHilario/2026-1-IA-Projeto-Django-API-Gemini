from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="chat_index"),
    path("limpar/", views.clear_history, name="clear_history"),
]
