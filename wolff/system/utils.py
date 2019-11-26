from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
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


class GenericForeignKeyMixin(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.CharField(max_length=200)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True
