from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginUser.as_view(), name='api_login'),
    path('profile/', ProfileView.as_view(), name='api_profile'),
    path('register/', RegisterUser.as_view(), name='api_register'),
    path('validate-username/', validate_username, name='validate_username'),
]
