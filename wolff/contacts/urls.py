from django.urls import path

from .views import ContactCreateView, ContactDetailView, ContactListView, ContactUpdateView


app_name = 'contacts'
urlpatterns = [
    path('new/', ContactCreateView.as_view(), name='create'),
    path('<str:pk>/edit/', ContactUpdateView.as_view(), name='update'),
    path('<str:pk>/', ContactDetailView.as_view(), name='detail'),
    path('', ContactListView.as_view(), name='index'),
]
