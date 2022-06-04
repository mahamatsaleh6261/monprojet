from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("comptes.urls")),
    path("staffs/", include("staffs.urls")),
    path("parcours/", include("parcours.urls")),
    path("cours/", include("cours.urls")),
    path("enseignants/", include("enseignants.urls")),
    path("etudiants/", include("etudiants.urls")),
    path("evaluations/", include("notes.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

