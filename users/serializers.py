from .models import UserProfile
from rest_framework import serializers
from WechatAPI.Login import WXLogin
from django.conf import settings

class UserSerializer(serializers.HyperlinkedModelSerializer):
    code = serializers.CharField(max_length=255)

    def create(self):
        code = self.validated_data['code']
        wxlogin = WXLogin(settings.WX_APPID,settings.WX_SECRET)
        openid = wxlogin.login(code)['openid']
        self.validated_data['openid'] = openid
        del self.validated_data['code']
        return UserProfile.objects.create(**self.validated_data)

    class Meta:
        model = UserProfile
        fields = ['code', 'nickName', 'avatarUrl', 'description', 'school']


class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)
