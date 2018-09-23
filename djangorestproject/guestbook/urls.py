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
from . import views
from rest_framework import routers

urlpatterns = [
    path("home/", views.home, name="home"),
    path("", views.index, name="index"),
    path("sign/", views.sign, name="sign"),
    path("todoindex/", views.todoindex, name="todoindex"),
    # """Not yet implemented """
    path("add", views.addtodo, name="add"),
    path("deletecomplete", views.deletecompleted, name="deletecomplete"),
    path("deleteall", views.deleteall, name="deleteall"),
    path("complete/<todo_id>", views.completetodo, name="complete"),
    path("updatenote", views.updatenote, name="updatenote")
]
