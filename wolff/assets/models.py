from uuid import uuid4

from django.db import models

from django_extensions.db.models import ActivatorModel

from .utils import costing_methods_as_choices
from system.utils import (
    NameAsStrMixin, CompanyFieldMixin, GenericForeignKeyMixin)


class UnitOfMeasure(NameAsStrMixin, CompanyFieldMixin):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)


class Item(NameAsStrMixin, CompanyFieldMixin, ActivatorModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=19, decimal_places=5, blank=True)
    unit_of_measure = models.ForeignKey(
        UnitOfMeasure, on_delete=models.PROTECT)
    costing_method = models.CharField(
        max_length=20,
        choices=costing_methods_as_choices,
        default='FIFO',
        blank=True)


class ItemTransaction(GenericForeignKeyMixin):
    quantity_in = models.DecimalField(max_digits=19, decimal_places=5)
    quantity_out = models.DecimalField(max_digits=19, decimal_places=5)
    cost = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    date = models.DateField()
    inventory_from = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='transactions',
        blank=True)
