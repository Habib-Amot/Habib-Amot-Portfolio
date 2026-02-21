from django.contrib.auth import get_user_model

User = get_user_model()

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from applications.users.models import Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']    


class RegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

        extra_kwargs = {
            'password':{
                'write_only': True,
            }
        }
    
    def validate(self, attrs):
        # making confirmation that the provided password is the same as the confirm password field
        if self.initial_data['confirm-password'] and self.initial_data['confirm-password'] != attrs['password']:
            raise serializers.ValidationError({"confirm-password": "The provided password do not match"})
        
        return super().validate(attrs)
    

class TransactionSerializer(ModelSerializer):
    source = UserSerializer(read_only=True)
    destination = UserSerializer(read_only=True)
    
    class Meta:
        model = Transaction
        fields = ['amount', 'source', 'destination', 'timestamp', 'transaction_type', 'transaction_status']
