#!coding=utf8
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.settings import api_settings
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework import status

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserView(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        code = request.data.get("code")
        user = authenticate(code=code)
        if user:
            login(request, user)
            jwt = jwt_encode_handler(jwt_payload_handler(user))
            return Response({'token': jwt})
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            jwt = jwt_encode_handler(jwt_payload_handler(user))
            resp = {
                "token": jwt
            }
            return Response(resp)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserUpdate(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def update(self, request):
        return Response({"a": 1})
