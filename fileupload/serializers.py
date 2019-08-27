# -*- coding: utf-8 -*-

from .models import *
from rest_framework import serializers


class UploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadModel
        fields = '__all__'

