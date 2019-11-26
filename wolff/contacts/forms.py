from django.forms import ModelForm

from .models import Contact


class ContactModelForm(ModelForm):

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

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        obj = super().save(*args, **kwargs)
        if self.request:
            obj.sys_company = self.request.user.currently_loggedin_company
        obj.save()

        return obj
