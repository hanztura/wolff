from django.urls import path

from .views import HomeTemplateView

app_name = 'system'
urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home')
]
