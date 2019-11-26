from django.urls import path

from .views import AccountCreateView, AccountDetailView, AccountListView, AccountUpdateView


app_name = 'accounting'
urlpatterns = [
    path('chart-of-accounts/new/', AccountCreateView.as_view(), name='coa_create'),
    path('chart-of-accounts/<int:pk>/edit/', AccountUpdateView.as_view(), name='coa_update'),
    path('chart-of-accounts/<int:pk>/', AccountDetailView.as_view(), name='coa_detail'),
    path('chart-of-accounts/', AccountListView.as_view(), name='coa_index'),
]
