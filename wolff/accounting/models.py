from enum import Enum
from uuid import uuid4

from django.db import models

from django_extensions.db.models import TimeStampedModel

from system.utils import (
    CompanyFieldMixin, NameAsStrMixin, GenericForeignKeyMixin)


class NormalBalance(Enum):
    debit = 'Debit'
    credit = 'Credit'


class AccountType(NameAsStrMixin, models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False)
    name = models.CharField(max_length=50, unique=True)
    normal_balance = models.CharField(
        max_length=5, choices=[(c.name, c.value) for c in NormalBalance])


class Account(CompanyFieldMixin, models.Model):
    title = models.CharField(max_length=50)
    account_type = models.ForeignKey(
        AccountType, on_delete=models.PROTECT, related_name='accounts')
    is_contra_account = models.BooleanField(default=False, blank=True)
    is_cash_account = models.BooleanField(default=False, blank=True)

    def __str_(self):
        return self.title


class Journal(CompanyFieldMixin, TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    series = models.SmallIntegerField(blank=True)
    code = models.CharField(max_length=50, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.code


class JournalItem(TimeStampedModel, GenericForeignKeyMixin):
    journal = models.ForeignKey(
        Journal, on_delete=models.PROTECT, related_name='items')
    account = models.ForeignKey(
        Account, on_delete=models.PROTECT, related_name='journals')
    debit = models.DecimalField(max_digits=14, decimal_places=2)
    credit = models.DecimalField(max_digits=14, decimal_places=2)
