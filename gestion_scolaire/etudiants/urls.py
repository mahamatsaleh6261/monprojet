from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    etudiant_list_view,
    etudiant_detail_view,
    etudiant_inscription_view,
    etudiant_update_view,
    etudiant_matiere_view,
    etudiant_note_view,
)

app_name = "etudiants"
urlpatterns = [
    path("ajouter", etudiant_list_view, name="ajouter"),
    path("", etudiant_list_view, name="etudiants"),
    path("matieres/", etudiant_matiere_view, name="matieres"),
    path("notes/", etudiant_note_view, name="notes"),
    path("<int:pk>/", etudiant_detail_view, name="etudiant"),
    path("<int:pk>/inscription/", etudiant_inscription_view, name="inscription"),
    path("<int:pk>/modifier/", etudiant_update_view, name="editer"),
]
