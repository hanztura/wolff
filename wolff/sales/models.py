from uuid import uuid4

from django.db import models

from assets.models import Item
from contacts.models import Contact
from system.utils import CompanyFieldMixin


class Invoice(CompanyFieldMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    series = models.SmallIntegerField(blank=True)
    code = models.CharField(max_length=50, blank=True)
    date = models.DateField()
    contact = models.ForeignKey(
        Contact, on_delete=models.PROTECT, related_name='sales_invoices')

    def __str__(self):
        return self.code


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(
        Invoice, on_delete=models.PROTECT, related_name='items')
    item = models.ForeignKey(
        Item, on_delete=models.PROTECT, related_name='invoices')
    qty = models.DecimalField(max_digits=19, decimal_places=5)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    discount_rate = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True)
    discount_amount = models.DecimalField(
        max_digits=14, decimal_places=2, blank=True)
    tax_rate = models.DecimalField(max_digits=17, decimal_places=5, blank=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
