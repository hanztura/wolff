from django.contrib import admin

from .models import User, Company, Setting

admin.site.register(Company)
admin.site.register(Setting)
admin.site.register(User)
