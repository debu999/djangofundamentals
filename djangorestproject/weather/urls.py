from django.urls import path, re_path, include
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path("index", views.wtindex, name="wtindex"),
    path("login/", LoginView.as_view(), name="wtlogin"),
    path("mail/", views.sendmail, name="wtmail")
]
