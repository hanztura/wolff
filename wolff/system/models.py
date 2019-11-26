from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser

from simple_history.models import HistoricalRecords

from .helpers import SingletonModel


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(AbstractUser):
    currently_loggedin_company = models.ForeignKey(
        Company, on_delete=models.PROTECT, null=True)


class Setting(SingletonModel):
    initial_data_runned = models.BooleanField(default=False, blank=True)
    history = HistoricalRecords()
