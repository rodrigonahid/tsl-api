from django.urls import path

from .views import RegistrationView, VerifyEmail

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = 'authentication'
urlpatterns = [
    path('', RegistrationView.as_view(), name='registration_view'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('verify-email/', VerifyEmail.as_view(), name='verify-email')
]