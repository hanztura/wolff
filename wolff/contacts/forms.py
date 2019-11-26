from django.forms import ModelForm

from .models import Contact
from system.utils import SaveCompanyFormMixin


class ContactModelForm(SaveCompanyFormMixin, ModelForm):

    class Meta:
        model = Contact
        fields = [
            'last_name',
            'first_name',
            'middle_name',
            'is_individual',
            'registered_name',
        ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['is_individual'].initial = True
