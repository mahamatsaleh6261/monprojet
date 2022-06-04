from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    staff_create_view,
    staff_list_view,
    staff_detail_view,
    staff_dashboard_view,
)

app_name = "staffs"
urlpatterns = [
    path("ajouter", staff_list_view, name="ajouter"),
    path("", staff_list_view, name="staffs"),
    path("<int:pk>/", staff_detail_view, name="staff"),
    path("tableau-de-bord", staff_dashboard_view, name="dashboard"),
]
