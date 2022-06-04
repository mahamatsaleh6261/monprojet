from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    enseignant_create_view,
    enseignant_list_view,
    enseignant_dashboard_view,
    enseignant_detail_view,
    enseignant_update_view,
    enseignant_matiere_list_view,
)

app_name = "enseignants"
urlpatterns = [
    path("ajouter/", enseignant_list_view, name="ajouter"),
    path("", enseignant_list_view, name="enseignants"),
    path("dashboard/", enseignant_dashboard_view, name="dashboard"),
    path("matieres/", enseignant_matiere_list_view, name="matieres"),
    path("<int:pk>/", enseignant_detail_view, name="enseignant"),
    path("<int:pk>/modifier/", enseignant_update_view, name="editer"),
]
