from django.db import models
from datetime import datetime
from django.utils import timezone
import pytz


class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    createdate = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title[:50]


class Posts1(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    createdate = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        verbose_name_plural = "Posts1"

    def __str__(self):
        return self.title[:50]
