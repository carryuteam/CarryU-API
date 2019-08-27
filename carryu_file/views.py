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

    @action(detail=False, methods=['get'])
    def search(self, request):
        name=request.data.get('name')
        cost=request.data.get('cost')
        school=request.data.get('school')        
        grade=request.data.get('grade')   
        tags=request.data.get('tags')            
        page=request.data.get('page')
        pagesize=request.GET.get('pagesize',1)
        
        print(pagesize)
        if pagesize is None:
            return Response({"error_code": 3})

        search_dict = dict()
        if name:
            search_dict['name'] = name
        if cost:
            search_dict['cost'] = cost
        if school:
            search_dict['school'] = school
        if grade:
            search_dict['grade'] = grade

        search_res = Resource.objects.filter(**search_dict)
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
        
        