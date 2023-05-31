from django.contrib.auth import authenticate
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from django.views.decorators.csrf import csrf_exempt

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginUser(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
        return Response({'error': 'Invalid credentials'}, status=400)


class RegisterUser(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProfileSerializer


class ProfileView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile


@csrf_exempt
def validate_username(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username', None)
        if username:
            is_taken = User.objects.filter(username__iexact=username).exists()
            return JsonResponse({'is_taken': is_taken})
    return JsonResponse({'error': 'Invalid request'})
