from uuid import uuid4

from django.db import models
from django.urls import reverse_lazy

from system.utils import CompanyFieldMixin


class Contact(CompanyFieldMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    last_name = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    middle_name = models.CharField(max_length=50, blank=True)
    is_individual = models.BooleanField(default=True, blank=True)
    registered_name = models.CharField(max_length=200, blank=True)

    @property
    def name(self):
        if self.is_individual:
            name = '{}, {}'.format(self.last_name, self.first_name)
        else:
            name = self.registered_name
        return name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('contacts:detail', args=[self.pk, ])
