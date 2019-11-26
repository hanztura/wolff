from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import Account, AccountModelForm
from system.utils import AddRequestToForm, SuccessFormOperationMixin


class AccountCreateView(SuccessFormOperationMixin, AddRequestToForm, CreateView):
    model = Account
    form_class = AccountModelForm

    def get_success_url(self):
        return reverse_lazy('accounting:coa_update', args=[self.object.pk, ])


class AccountUpdateView(SuccessFormOperationMixin, AddRequestToForm, UpdateView):
    model = Account
    form_class = AccountModelForm


class AccountListView(ListView):
    model = Account

    def get_queryset(self):
        q = super().get_queryset()
        q = q.select_related('account_type')

        return q


class AccountDetailView(DetailView):
    model = Account

    def get_queryset(self):
        q = super().get_queryset()
        q = q.select_related('account_type')

        return q
