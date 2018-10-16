from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

from .views import gamedetails, welcome, invite, acceptinvitation

urlpatterns = [
    path("gamedetails/", gamedetails, name="gamedetails"),
    re_path(r"login$", LoginView.as_view(template_name="registration/login_form.html",
                                         extra_context={"next": "home"}), name="player_login"),
    re_path(r"logout$", LogoutView.as_view(), name="player_logout"),
    path("home/", welcome, name="welcome"),
    re_path("^$", welcome, name="welcome1"),
    re_path(r"invite$", invite, name="player_invite"),
    re_path(r"acceptinvitation/(?P<id>\d+)/$", acceptinvitation, name="player_acceptinvitation")
]
