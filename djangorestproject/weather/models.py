import random

from django.db import models

rngvar = range(2000000)


def my_random_key():
    global rngvar
    return random.choice(rngvar)


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ("add", "change", "delete", "view")

class City(models.Model):
    name = models.CharField(max_length=100)
    cityid = models.IntegerField()
    populationcount = models.IntegerField(default=my_random_key)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, default=1)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "cities"
        default_permissions = ("add", "change", "delete", "view")
