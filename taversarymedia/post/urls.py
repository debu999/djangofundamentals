from django.urls import path, include, re_path

from . import views

urlpatterns = [
    re_path("^$", views.index, name="index"),
    path("details/<int:id>", views.details, name="details")
]
