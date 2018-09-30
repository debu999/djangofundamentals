from django.db import models
from django.utils import timezone


class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Name: {} Id: {}".format(self.name, self.id)


class Company(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name


class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)
    datecreated = models.DateTimeField(auto_now_add=True)
    lastupdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class Course(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    order = models.IntegerField()

    def __str__(self):
        return self.title


class Lecture(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    order = models.IntegerField()
    code_link = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.title


def ipyhistory(lastn=None):
    import readline
    assert lastn is None or (isinstance(lastn, int) and lastn > 0), "Only positive numbers are allowed."
    hlen = readline.get_current_history_length()
    flen = len(str(lastn)) if lastn else len(str(hlen))
    for r in range(hlen) if not lastn else range(hlen)[-lastn:]:
        print(": ".join([str(r + lastn - hlen + 1 if lastn else r).rjust(flen), readline.get_history_item(r)]))
