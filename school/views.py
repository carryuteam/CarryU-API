from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.decorators import action
from school.models import School
from school.serializers import SchoolSerializer,SchoolCodeSerializer
import json
from django.db.models import Count
# Create your views here.

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [permissions.AllowAny]    

    def get(self, request):
        code=request.GET.get('code')
        try:
            sc=School.objects.get(code=code)
        except BaseException:
            return Response({"error_code": 1})      
        return Response({
            "error_code": 0,
            "data": SchoolSerializer(sc).data           
        })

    def getAll(self, request):
        schoolCode=request.GET.get('schoolCode')
        if schoolCode is not None:
            sc=School.objects.filter(schoolCode=schoolCode)
        else:
            sc=School.objects.all()
        return Response({
            "error_code": 0,
            "data": SchoolSerializer(sc,many=True).data           
        })
    def getSchool(self, request):
        sc=School.objects.values('schoolCode','schoolName').annotate().distinct()
        print(sc)
        return Response({
            "error_code": 0,
            "data": SchoolCodeSerializer(sc,many=True).data    
        })
    
class AdminSchoolViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def add(self, request):
        if request.user.is_staff != 1:
            return Response({"error_code": 2})

        sc=SchoolSerializer(data=json.loads(request.body.decode()),many=True)
        print(json.loads(request.body.decode()))
        print(request.body)
        if sc.is_valid():
            print(sc.validated_data)
            sc.save()
            return Response({
                "error_code": 0,
                "data": sc.validated_data        
            })
        else: 
            return Response({"error_code": 1})     

