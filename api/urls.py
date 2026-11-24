from django.urls import path
from .views import *    

urlpatterns = [
    path('transactions/', TransactionListCreateAPIView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionRetrieveUpdateDestroyAPIView.as_view(), name='transaction-retrieve-update-destroy'),
    path('wallets/', WalletListView.as_view(), name='wallet-list'),
]   