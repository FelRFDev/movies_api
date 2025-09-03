from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('token_obtain/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('token_refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token_verify/', TokenVerifyView.as_view(), name='token-verify'),
]
