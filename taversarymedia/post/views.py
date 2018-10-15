from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Posts


def index(request):
    # return HttpResponse("Hola A simple posts app. Hello again.")
    posts = Posts.objects.all()[:10]
    context = {"posts": posts, "title": "Mind Blowing Djanog Blog App..."}
    return render(request, "post/index.html", context=context)


def details(request, id):
    p = Posts.objects.get(id=id)
    context = {"p": p, "title": f"Post {p.id}.{p.title[:10]} Details..."}
    return render(request, "post/details.html", context=context)
