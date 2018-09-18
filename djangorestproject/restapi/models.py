from django.db import models


# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(name="firstname", max_length=20)
    lastname = models.CharField(name="lastname", max_length=20)
    sid = models.IntegerField(name="sid", null=False)

    def __repr__(self):
        return "{} {}".format(self.firstname, self.lastname)

    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)
