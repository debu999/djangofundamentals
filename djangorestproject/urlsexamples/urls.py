from django.urls import path, re_path
from urlsexamples import views

urlpatterns = [
    path("profile/35", views.profile35),
    path("profile/<int:val>", views.profileval),
    path("profile/<slug:slg>", views.profileslg),
    path("profile/<str:valu>", views.profilevalu),
    re_path("^profile/(?P<uid>[\w_-]+)?/?(?P<unm>\w+|)?/?$", views.profile)
]
