from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="incidents_index"),
    path("limpar/", views.clear, name="incidents_clear"),
]
