from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Popularity, Language, Programmer
from .serializers import LanguageSerializer, ProgrammerSerializer, PopularitySerializer


# Create your views here.


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PopularityView(viewsets.ModelViewSet):
    queryset = Popularity.objects.all()
    serializer_class = PopularitySerializer
    permission_classes = (permissions.IsAuthenticated,)


class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
    permission_classes = (permissions.IsAdminUser,)


def index(request):
    return HttpResponse("Hello World!!!! You are in index page of languages app.")
