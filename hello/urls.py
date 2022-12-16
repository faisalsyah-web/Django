from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:nama>", views.sapa, name="sapa"),
    path("ais", views.ais, name="ais"),
    path("leslie", views.leslie, name="leslie"),
]
