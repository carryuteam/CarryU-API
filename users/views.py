#!coding=utf8
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


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
            user = serializer.create()
            serializer = TokenSerializer(data={
                'token': jwt_encode_handler(jwt_payload_handler(user))
            })
            return Response(serializer.data)
        print(serializer.errors)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

