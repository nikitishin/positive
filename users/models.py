from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    job_position = models.ForeignKey('JobPosition', on_delete=models.PROTECT, null=True, blank=True)

class JobPosition(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return f'{self.name}'
# Create your models here.
