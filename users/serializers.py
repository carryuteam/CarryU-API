#!coding=utf-8
from .models import UserProfile
from rest_framework import serializers
from WechatAPI.Login import WXLogin
from django.conf import settings


class UserSerializer(serializers.HyperlinkedModelSerializer):
    #code = serializers.CharField(max_length=255, required=False)

    def update(self, instance, validated_data=None):
        for attr, value in validated_data.items():
            if attr != "code" or attr != "openid":
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = UserProfile
        fields = ['openid', 'nickName', 'avatarUrl', 'description', 'school', 'grade', 'gender']

class ChangeUserSerializer(serializers.HyperlinkedModelSerializer):

    def update(self, instance, validated_data=None):
        for attr, value in validated_data.items():
            if attr != "code" or attr != "openid":
                setattr(instance, attr, value)
        instance.save()
        return instance
        
    class Meta:
        model = UserProfile
        fields = ['nickName', 'avatarUrl', 'description', 'school', 'grade', 'gender']

class FullUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['openid','nickName', 'avatarUrl', 'description', 'school', 'grade', 'gender', 'coin', 'create_time', 'login_time']
