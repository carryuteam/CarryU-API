#!coding=utf8
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.settings import api_settings
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth import authenticate, login

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]



    def list(self, request):
        code = request.data.get("code")
        is_first=[0]
        user = authenticate(code=code,is_first=is_first)
        print("xxx")
        print(is_first[2])
        if user:
            login(request, user)
            jwt = jwt_encode_handler(jwt_payload_handler(user))
            return Response({'error_code':0,'data':{'token': jwt,'openid':user.openid,'is_first': is_first[1]}})
        elif is_first[1]==1:
            return Response({'error_code':0,'data':{'openid':is_first[2],'is_first': is_first[1]}})
        return Response({"error_code": 401, "error": "登陆失败"})

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            jwt = jwt_encode_handler(jwt_payload_handler(user))
            resp = {
                "token": jwt
            }
            return Response(resp)
        return Response({"error_code": 401, "error": "注册失败"})


class UserUpdateViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def update(self, request):
        user = request.user
        print(user.openid)
        serializer = ChangeUserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            ret = {
                "error_code": 0,
                "data": serializer.data
            }
            return Response(ret)
        return Response(
            {
                "error_code": 1,
                "error": serializer.errors,
                "data": serializer.data
            }
        )
    
    def getdetail(self, request):
        id=request.GET.get('openid')
        user=None
        if id is None:
            user = request.user
        else:
            try:
                user = UserProfile.objects.get(openid=id)
            except BaseException:
                return Response({"error_code": 1})
        serializer = FullUserSerializer(user)
        return Response({
            "error_code": 0,
            "data": serializer.data
        })
    
    def addcoin(self, request):
        user = request.user
        if user.coin is None:
            user.coin = 10
        user.coin += 1000
        user.save()
        return Response({"error_code": 0})
    
