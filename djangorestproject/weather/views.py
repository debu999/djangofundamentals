import os
from math import floor

from django.db.models import When, Case
from django.shortcuts import render
import requests
from pprint import pprint as pp
import random
from .forms import CityForm

# Create your views here.
from weather.models import City
from django.core.mail import send_mail


def wtindex(request):
    url = "http://api.openweathermap.org/data/2.5/weather?id=" \
          "{}&units=metric&APPID={}"

    def get_randomcity(numcty=5):
        mxid = City.objects.all().order_by("-id")[0].id
        idlst = [floor(mxid * random.random()) for _ in range(numcty)]
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(idlst)])
        return City.objects.filter(id__in=idlst).order_by(preserved)

    # city = "Republic of India"
    # cityid = 1269750
    # city = "Kathmandu"
    # cityid = 1283240
    cities = list()
    form = None
    cityname = None
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            cityname = form.cleaned_data["name"]
            cities = City.objects.all().filter(name=cityname)

    if request.method == "GET":
        form = CityForm()
        cities = get_randomcity(2)

    weather_data = list()

    for city in cities:
        r = requests.get(url.format(city.cityid, os.environ.get("WEATHERAPI"))).json()
        pp(r)
        citywtdata = {
            "city": city.name,
            "temperature": r.get("main").get("temp"),
            "description": r.get("weather")[0].get("description"),
            "icon": r.get("weather")[0].get("icon"),
            "cityid": city.cityid
        }

        weather_data.append(citywtdata)

    context = {"citywtdata": weather_data, "form": form}
    if not len(cities):
        context["citynotfound"] = "City {} not found in weathermap. Please review.".format(cityname)

    pp(context)
    return render(request, "weather/index.html", context=context)


def sendmail(request):
    send_mail("hello from Debabrata...", "Hello there its a Automated Request", "debu999@gmail.com",
              ["jabe@spindl-e.com", ],
              fail_silently=False)
    return render(request, "weather/index.html")
