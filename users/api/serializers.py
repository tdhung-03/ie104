from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'name', 'phone_number', 'address']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        user = User.objects.create_user(password=password, **user_data)
        profile = Profile.objects.create(user=user, **validated_data)
        profile.username = user_data["username"]
        profile.email = user_data["email"]
        profile.save()
        return profile
