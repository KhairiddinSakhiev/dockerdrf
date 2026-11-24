from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import CustomUser
from api.models import Wallet

@receiver(post_save, sender=CustomUser)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)