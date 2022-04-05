from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegistrationSerializer
from .models import User

import jwt

class RegistrationView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data
        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        # Email part
        user = User.objects.get(email=serializer.data['email'])
        token = RefreshToken.for_user(user).access_token

        relativeLink = reverse("users:verify-email")
        currentDomain = get_current_site(request).domain
        absurl = "http://" + currentDomain + relativeLink + "?token=" + str(token)

        data = {
          'email_body': 'Hi,' + user_data['username'] + 'Use the link below to verify your account: \n' + absurl,
          'email_subject': user_data['username'] + ', Activate your Wall App account',
        }

        email = EmailMessage(subject=data['email_subject'], body=data['email_body'], to=[serializer.data["email"]] )

        email.send()

        print(token)

        return Response({"message": "Account created, check your email"}, status=status.HTTP_201_CREATED)

class VerifyEmail(generics.GenericAPIView):
    def get(self, request):
        token = request.GET.get('token')
        
        try:
            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms='HS256')
            print('payload', str(payload))
            user = User.objects.get(id = payload['user_id'])
            
            if not user.is_active:
                user.is_active = True
                user.save()

            return Response({"message": "Account activated"}, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError as e:
            # print(e)
            return Response({'error': 'Activations link expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as e:
            print(e)
            return Response({'error': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)