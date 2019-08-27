#!coding=utf-8
from .models import UserProfile
from rest_framework import serializers
from WechatAPI.Login import WXLogin
from django.conf import settings


class UserSerializer(serializers.HyperlinkedModelSerializer):
    code = serializers.CharField(max_length=255)

    def create(self, validated_data=None):
        if validated_data is None:
            validated_data = self.validated_data
        data = validated_data  # 创建副本
        code = data['code']
        wxlogin = WXLogin(settings.WX_APPID, settings.WX_SECRET)
        openid = wxlogin.login(code)['openid']
        user = UserProfile.objects.get(openid=openid)
        if user:
            return user
        data['openid'] = openid
        print(data)
        del data['code']  # 将Code变为OpenID
        return UserProfile.objects.create(**data)

    def update(self, instance, validated_data=None):
        instance.nickName = validated_data['nickName']
        instance.avatarUrl = validated_data['avatarUrl']
        instance.description = validated_data['description']
        instance.school = validated_data['school']
        instance.save()
        return instance

    class Meta:
        model = UserProfile
        fields = ['code', 'nickName', 'avatarUrl', 'description', 'school']
