from django.db import models
from django.conf import settings


class Event(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateTimeField()


class Ticket(models.Model):
    date = models.DateTimeField(auto_now = True)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
