from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import Contact, ContactModelForm
from system.utils import AddRequestToForm


class ContactCreateView(AddRequestToForm, CreateView):
    model = Contact
    form_class = ContactModelForm


class ContactUpdateView(AddRequestToForm, UpdateView):
    model = Contact
    form_class = ContactModelForm


class ContactListView(ListView):
    model = Contact


class ContactDetailView(DetailView):
    model = Contact
