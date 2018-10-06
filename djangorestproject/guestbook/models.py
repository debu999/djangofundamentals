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
    """
    param: lastn Defaults to None i.e full history. If specified then returns lastn records from history.
           Also takes -ve sequence for first n history records.
    """
    import readline
    assert lastn is None or isinstance(lastn, int), "Only integers are allowed."
    hlen = readline.get_current_history_length()

    is_neg = lastn is not None and lastn < 0
    if not is_neg:
        flen = len(str(hlen)) if not lastn else len(str(lastn))
        for r in range(1, hlen + 1) if not lastn else range(1, hlen + 1)[-lastn:]:
            print(": ".join([str(r if not lastn else r + lastn - hlen).rjust(flen), readline.get_history_item(r)]))
    else:
        flen = len(str(-hlen))
        for r in range(1, -lastn + 1):
            print(": ".join([str(r).rjust(flen), readline.get_history_item(r)]))
