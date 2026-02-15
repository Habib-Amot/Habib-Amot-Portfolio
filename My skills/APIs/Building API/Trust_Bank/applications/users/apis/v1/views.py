from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from applications.users.serializers import RegistrationSerializer


# this view is made for browsers and not for any other script that does not run within a browser
class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(
                {'redirect': reverse('user-dashboard')}
            )
        
        else:
            return Response({
                'error': 'invalid credentials',
                'message': "Invalid username or password"
            }, status=status.HTTP_401_UNAUTHORIZED)


class RegistrationView(APIView):
    def post(self, request):
        # getting the submitted data from the user
        submitted_data = RegistrationSerializer(data=request.data)

        # running validations on the submitted data
        if submitted_data.is_valid():
            # saving the user to the database
            user = submitted_data.save()

            user_email: str = submitted_data.validated_data.get('email')

            message = "<h1>This is a test email from my backend</h1>"
            send_mail(
                subject='Test Email', 
                message=message, 
                from_email='habibgemini1@gmail.com', 
                recipient_list=[user_email]
            )

            # create a JWT token for the user 
            tokens = RefreshToken.for_user(user=user)
            return Response({
                "tokens": tokens, "message":"account created successfully", "redirect_to": reverse('user-dashboard')
                })
        
        else:
            return Response({"message":submitted_data._errors,}, status=status.HTTP_401_UNAUTHORIZED)


class UserDashboardView(APIView):
    def post(self, request):
        return Response('this is the user dashboard')
    
    def get(self, request):
        return Response('this is the user dashboad get page')
