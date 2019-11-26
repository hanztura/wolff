from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib import messages
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


class AddRequestToForm:

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class SaveCompanyFormMixin:

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        obj = super().save(*args, **kwargs)
        if self.request:
            obj.sys_company = self.request.user.currently_loggedin_company
        obj.save()

        return obj


class SuccessFormOperationMixin:
    def form_valid(self, form):
        msg = 'Successfully saved.'
        messages.success(
            self.request,
            msg)
        return super().form_valid(form)
