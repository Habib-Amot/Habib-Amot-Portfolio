from django.contrib.auth import get_user_model

from applications.users.models import Transaction
from applications.users.serializers import TransactionSerializer

User = get_user_model()


def user_profile_summary(user):
    username = user.username
    balance = user.profile.account_balance
    recent_transactions = Transaction.objects.filter(user=user).order_by('-timestamp')[2]

    return {
        "username": username,
        "balance": balance,
        "recent_transactions":[
            TransactionSerializer(tnx) for tnx in recent_transactions
        ]
    }