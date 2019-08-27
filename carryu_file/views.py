from django.shortcuts import render
from rest_framework.response import Response
from carryu.models import User,Resource,ResouceFolder
from carryu_file.serializers import UserSerializer, ResourceSerializer, ResourceListSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.decorators import action
# Create your views here.
class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def search(self, request):
        name=request.GET.get('name')
        cost=request.GET.get('cost')
        school=request.GET.get('school')        
        grade=request.GET.get('grade')   
        tags=request.GET.get('tags')            
        page=request.GET.get('page')
        pagesize=request.GET.get('pagesize')
        order=request.GET.get('order')

        
        print(pagesize)
        if pagesize is None:
            return Response({"error_code": 3})

        search_dict = dict()
        if name:
            search_dict['name'] = name
        if cost:
            search_dict['cost__lte'] = cost
        if school:
            search_dict['school'] = school
        if grade:
            search_dict['grade'] = grade

        search_res=None
        if order:
            if order==1:
                search_res = Resource.objects.filter(**search_dict).order_by('grade')
            else if order==2:
                search_res = Resource.objects.filter(**search_dict).order_by('cost')
        
        paginator = Paginator(search_res, pagesize)
        total = paginator.count

        try:
            res = paginator.page(page)
        except PageNotAnInteger:
            res = paginator.page(1)
        except EmptyPage:
            res = paginator.page(paginator.num_pages)
        
        serializer = ResourceListSerializer(res, many=True)
        return Response({
            "error_code": 0,
            "resources": serializer.data,
            "total": total
        })

    def details(self, request):
        id = request.GET.get('resid')
        print(id)
        if id is None:
            return Response({"error_code": 3})
        try: 
            res = Resource.objects.get(resid=id)
        except BaseException:
            return Response({"error_code": 1})
        
        print("ok")
        serializer = ResourceSerializer(res)
        return Response({
            "error_code": 0,
            "resources": serializer.data
        })
