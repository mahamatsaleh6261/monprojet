from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    evaluation_create_view,
    evaluation_list_view,
    evaluation_note_create_view,
)

app_name = "notes"
urlpatterns = [
    path("<int:pk>/ajouter", evaluation_create_view, name="ajouter"),
    path("<int:pk>/", evaluation_list_view, name="evaluations"),
    path("<int:pk>/notes/", evaluation_note_create_view, name="notes"),
]
