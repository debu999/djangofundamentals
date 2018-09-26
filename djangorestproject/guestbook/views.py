from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .models import Comment, Todo
from . import models
from .forms import CommentForm, TodoForm, NewTodoForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


def home(request):
    return HttpResponse("Hello World from guestbook app.")


def index(request):
    comments = models.Comment.objects.order_by("-date_added")
    context = {"comments": comments}
    return render(request, "guestbook/index.html", context=context)


def sign(request):
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            newcomment = Comment(name=form.cleaned_data["name"],
                                 comment=form.cleaned_data["comment"])
            newcomment.save()
            return redirect("index")

    else:
        form = CommentForm()
    context = {"form": form}
    return render(request, "guestbook/sign.html", context=context)


def add(request):
    pass


def todoindex(request):
    todo_list = Todo.objects.order_by("id")
    # form = TodoForm()
    form = NewTodoForm()
    context = {"todo_list": todo_list, "form": form}
    return render(request, "guestbook/todoindex.html", context=context)


@require_POST
def addtodo(request):
    # form = TodoForm(request.POST)
    # text = request.POST["text"]
    # print(text)
    pk = request.POST.get("id_todo", 0)
    if pk:
        todoobj = Todo.objects.get(pk=pk)
        newtodoform = NewTodoForm(request.POST, instance=todoobj)
    else:
        newtodoform = NewTodoForm(request.POST)

    if newtodoform.is_valid():
        newtodoform.save()

    return redirect("todoindex")


def completetodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect("todoindex")


def deletecompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect("todoindex")


def deleteall(request):
    Todo.objects.all().delete()

    return redirect("todoindex")


def updatenote(request):
    Todo.objects.all().delete()

    return redirect("todoindex")


def register(request):
    if request.method == "GET":
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect("todoindex")

    context = {"form": form}
    return render(request, "registration/register.html", context)
