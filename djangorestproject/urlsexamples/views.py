from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def profile(request, uid="", unm=""):
    res = "<h1>This is urlexamples profile page... Hola!!!!!</h1>"
    if uid:
        res = "".join([res, "<br><h2>Welcome user: uid-{}</h2>".format(uid)])

    if unm:
        res = "".join([res, "<br><h2>Howdy unm-{}".format(unm)])

    return HttpResponse(res)


def profile35(request):
    res = "<h1>This is urlexamples profile page... Hola!!!!!</h1><br><h2>Its profile 35"

    return HttpResponse(res)


def profileval(request, val=-1):
    res = "<h1>This is urlexamples profile page... Hola!!!!!</h1><br><h2>Its profile val: val={}".format(val)

    return HttpResponse(res)


def profilevalu(request, valu=""):
    res = "<h1>This is urlexamples profile page... Hola!!!!!</h1><br><h2>Its profile valu: valu={}".format(valu)

    x = 123
    print(f"{x}")

    return HttpResponse(res)


def profileslg(request, slg="-"):
    res = "<h1>This is urlexamples profile page... Hola!!!!!</h1><br><h2>Its profile slug: slug={}".format(slg)

    return HttpResponse(res)
