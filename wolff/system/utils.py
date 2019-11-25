from django.db import models

from .models import Company


class CompanyFieldMixin(models.Model):
    sys_company = models.ForeignKey(
        Company, on_delete=models.PROTECT, editable=False)

    class Meta:
        abstract = True


class NameAsStrMixin:

    def __str__(self):
        return self.name
