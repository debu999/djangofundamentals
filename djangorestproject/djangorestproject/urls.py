"""djangorestproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns

from restapi import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^employees/", views.EmployeeList.as_view()),
    path("wt/", include("weather.urls")),
    path('', include("languages.urls")),
    path('guestbook/', include("guestbook.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
    path("urlex/", include("urlsexamples.urls")),
    path("apiauth/", include("rest_framework.urls")),
    path("api/token", TokenObtainPairView.as_view()),
    path("api/token/refresh", TokenRefreshView.as_view()),
]
