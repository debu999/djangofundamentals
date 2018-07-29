from django.conf.urls import url, re_path

from .views import home

urlpatterns = [
    re_path(r"home$", home)
]