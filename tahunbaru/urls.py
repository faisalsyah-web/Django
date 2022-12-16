from django.urls import path
from . import views

urlpatterns = [path("", views.tahunBaru, name="tahun baru")]
