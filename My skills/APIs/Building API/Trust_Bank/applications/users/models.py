import uuid
from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User

from rest_framework_api_key.models import AbstractAPIKey


class UserAPIKey(AbstractAPIKey):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_key')


# this table is responsible for managing each transaction 
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transaction_source')
    destination = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transaction_destinationTra')
    description = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    transaction_type = models.CharField(max_length=20)
    transaction_id = models.UUIDField(max_length=200, unique=True, default=uuid.uuid4, editable=False)
    transaction_status = models.CharField(max_length=20, default='pending')

    def get_transaction_message(self):
        if self.user.pk == self.source.pk:
            return f"Transfer to {self.destination.username}"
        else:
            return f"Incoming Transfer from {self.source.username}"

    def __str__(self) -> str:
        return f"{self.transaction_type}: {self.get_transaction_message()}"


class Profile(models.Model):
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    account_number = models.CharField(max_length=20, unique=True)
    account_created_at = models.DateTimeField(auto_now_add=True)
    account_type = models.CharField(max_length=20, default='savings')

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
