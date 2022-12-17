from django.urls import path
from . import views


urlpatterns = [
    path("", views.tahunApp, name="tahunApp"),
    path("tmbh", views.tmbh, name="tambah"),
]
