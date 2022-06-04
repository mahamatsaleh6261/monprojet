from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import login_view, logout_view, activate_account_view, set_password_view, profil_detail_view

app_name = "comptes"
urlpatterns = [
    path("", login_view, name="login"),
    path("deconnexion", logout_view, name="logout"),
    path("profil/", profil_detail_view, name="profil"),
    path("activate/<uidb64>/<token>/", activate_account_view, name="activate"),
    path("set-password/<uidb64>/<token>/", set_password_view, name="set_password"),
]
