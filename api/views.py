from django.shortcuts import render

from .serializers import *
from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

class TransactionListCreateAPIView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    def perform_create(self, serializer):
        serializer.save(wallet=Wallet.objects.filter(user=self.request.user).first())
        
    def get_queryset(self):
        res = super().get_queryset()
        res = res.filter(user=self.request.user)
        return res

class TransactionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    
class WalletListView(ListAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer