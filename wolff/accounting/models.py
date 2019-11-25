from enum import Enum

from django.db import models

from system.utils import CompanyFieldMixin, NameAsStrMixin


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

    def __str_(self):
        return self.title
