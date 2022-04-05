from django.urls import path

from .views import RegistrationView, VerifyEmail

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = 'authentication'
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', RegistrationView.as_view(), name='registration_view'),
    path('verify-email/', VerifyEmail.as_view(), name='verify-email')
]