from django.db import models
from django.conf import settings


class ViberUser(models.Model):
    viber_id = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    language = models.CharField(max_length=32, null=True, blank=True)
    country = models.CharField(max_length=32, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_blocked = models.BooleanField(default=False, null=True, blank=True)
    primary_device_os = models.CharField(max_length=64, null=True, blank=True)
    device_type = models.CharField(max_length=64, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.phone_number}:{self.name}:{self.language}'

    # def language(self):
    #     return f'{self.language}'
