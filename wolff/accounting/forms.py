from django.forms.models import ModelForm

from .models import Account
from system.utils import SaveCompanyFormMixin


class AccountModelForm(SaveCompanyFormMixin, ModelForm):

    class Meta:
        model = Account
        fields = [
            'title',
            'account_type',
            'is_contra_account',
            'is_cash_account',
        ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['is_contra_account'].initial = False
        self.fields['is_cash_account'].initial = False
