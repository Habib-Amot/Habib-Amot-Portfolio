from django.urls import reverse
from django.db import transaction
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from applications.users.models import Profile
from applications.users.serializers import RegistrationSerializer
from applications.users.services.user_details import user_profile_summary
from applications.users.services.authentications import IsAuthenticatedOrHasAPIKey

@method_decorator(transaction.atomic, name='post')
class RegistrationView(APIView):
    def post(self, request):
        # getting the submitted data from the user
        submitted_data = RegistrationSerializer(data=request.data)

        # running validations on the submitted data
        if submitted_data.is_valid():
            # saving the user to the database
            user = submitted_data.save()

            # creating a profile for the user
            Profile.objects.create(user=user, account_number = '7033900263')
            """ user_email: str = submitted_data.validated_data.get('email')

            message = "<h1>This is a test email from my backend</h1>"
            send_mail(
                subject='Test Email', 
                message=message, 
                from_email='habibgemini1@gmail.com', 
                recipient_list=[user_email]
            ) """

            # create a JWT token for the user 
            tokens = RefreshToken.for_user(user=user)
            return Response({
                "tokens": {
                    'access': str(tokens.access_token),
                    "refresh": str(tokens)
                    }, 
                "message":"account created successfully", 
                "redirect_to": reverse('user-dashboard')
            })
        
        else:
            return Response({"message":submitted_data._errors,}, status=status.HTTP_401_UNAUTHORIZED)


class UserDashboardView(APIView):
    permission_classes = [IsAuthenticatedOrHasAPIKey]
    
    def get(self, request):
        user = request.user
        profile_summary = user_profile_summary(user=user)
        return Response(profile_summary)
