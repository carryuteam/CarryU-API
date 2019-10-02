from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from res.models import ResouceTag,Resource
from res.serializers import TagSerializer
from django.db import models

class ResourceTagViewSet(viewsets.ModelViewSet):
    queryset = ResouceTag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

    def addTag(self, request):
        tag = request.data.get('tag')
        ResouceTag.objects.get_or_create(tag=tag)
        return Response({"error_code": 0})
    
    def getTag(self, request):
        id=request.GET.get('tag')
        if id is not None:
            try:
                now=ResouceTag.objects.get(tag=id) 
            except BaseException:
                return Response({"error_code": 1})
            if now is not None:
                serializer=TagSerializer(now)
                return Response({
                    "error_code": 0,
                    "data": serializer.data
                })
            return Response({"error_code": 1})

    def searchTag(self, request):
        name=request.GET.get('tag')
        if name is not None:
            search_res = ResouceTag.objects.filter(tag__contains=name)
            serializer = TagSerializer(search_res, many=True)
            return Response({
                "error_code": 0,
                "data": serializer.data
            })
        return Response({"error_code": 1})

    def transTag(tagstring):
        arr=list(filter(None,tagstring.split(',')))
        ret=[]
        for tag in arr:
            try:
                now=ResouceTag.objects.get(tag=tag) 
            except BaseException:
                print("未找到")
                continue
            ret.append(now)
        print(ret)
        return ret

    def transStr(tags):
        ret=","
        for tag in tags:
            ret=ret+tag.tag+','
        return ret

    def addStr(tagstring):
        arr=list(filter(None,tagstring.split(',')))
        for tag in arr:
            try:
                now=ResouceTag.objects.get_or_create(tag=tag)
            except BaseException:
                print("xxxx")
                continue
        
    def upRes(res):
        tagstring=res.tags
        arr=ResourceTagViewSet.transTag(tagstring)
        tagstring=ResourceTagViewSet.transStr(arr)
        res.tags=tagstring
        res.save()
    
            
