from django.urls import path

from .views import (
    create_module,
    module_list_view,
    create_matiere,
    matiere_list_view,
    cours_dashboard_view,
    matiere_detail_view,
    matiere_view,
)


app_name = "cours"
urlpatterns = [
    path("modules/ajouter", module_list_view, name="ajouter_module"),
    path("modules", module_list_view, name="modules"),
    path("matieres/ajouter", matiere_list_view, name="ajouter_matiere"),
    path("matieres", matiere_list_view, name="matieres"),
    path("tableau-de-bord", cours_dashboard_view, name="dashboard"),
    path("mesma", matiere_view, name="mat"),
    path("matieres/<int:pk>/", matiere_detail_view, name="matiere"),
]
