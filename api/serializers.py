from rest_framework import serializers
from .models import *
from accounts.serializers import UserSerializer
from django.db.models import Sum

class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['id', 'is_active','wallet']
        

        

class WalletSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Wallet
        fields = ['id', 'user', 'balance', 'created_at',]
        read_only_fields = ['id', 'user', 'created_at']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['total_income'] = Transaction.objects.filter(type="income", wallet=instance).aggregate(Sum("amount"))
        representation['total_expence'] = Transaction.objects.filter(type="expense", wallet=instance).aggregate(Sum("amount"))
        return representation