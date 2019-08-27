from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
import os
from .serializers import *
from django.core.files import File
from django.conf import settings
from rest_framework.response import Response
from django.http import HttpResponse
import uuid


class UploadViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file = request.FILES.get("file", None)

        ext = os.path.splitext(file.name)[-1]
        name = uuid.uuid4().hex
        filename = name+ext
        pathname = os.path.join(settings.MEDIA_ROOT, filename)

        with open(pathname, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        data = {
            "uid": request.user.openid,
            "src": pathname
        }
        file = UploadSerializer(data=data)
        if file.is_valid():
            file.save()
            ret = {
                "error_code": 0,
                "data": file.data
            }
            return Response(ret)
        else:
            ret = {
                "error_code": 500,
                "error": file.errors
            }
            return Response(ret)

    def get(self, request, fid):
        file = UploadModel.objects.filter(id=fid)[0]
        src = file.src

        with open(src, 'rb') as f:
            file = File(f)

            response = HttpResponse(file.chunks(), content_type='APPLICATION/OCTET-STREAM')
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(src)
            response['Content-Length'] = os.path.getsize(src)

        return response

