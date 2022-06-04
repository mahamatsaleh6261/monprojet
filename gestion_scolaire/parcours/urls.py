from django.urls import path

from .views import (
    create_domain,
    domain_list_view,
    create_mention,
    mention_list_view,
    create_specialite,
    specialite_list_view,
    dashboard_view,
)

app_name = "parcours"
urlpatterns = [
    path("domaines/ajouter", domain_list_view, name="ajouter_domain"),
    path("domaines", domain_list_view, name="domains"),
    path("mentions/ajouter", mention_list_view, name="ajouter_mention"),
    path("mentions", mention_list_view, name="mentions"),
    path("specialites/ajouter", specialite_list_view, name="ajouter_specialite"),
    path("specialites", specialite_list_view, name="specialites"),
    path("", dashboard_view, name="dashboard"),
]
