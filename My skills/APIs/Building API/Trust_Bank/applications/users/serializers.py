from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


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
