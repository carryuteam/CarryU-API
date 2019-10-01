from django.shortcuts import render
from rest_framework.response import Response
from res.models import Resource,ResouceFolder
from res.serializers import UserSerializer, ResourceSerializer, ResourceListSerializer, ResouceFolderSerializer, ResourceURLSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.decorators import action
from res.tags import ResourceTagViewSet
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
        else:
            search_res = Resource.objects.filter(**search_dict)

        if pagesize is None:
            serializer = ResourceListSerializer(search_res, many=True)
            return Response({
                "error_code": 0,
                "data": serializer.data
            })

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
            "data": serializer.data,
            "total": total
        })

    def details(self, request):
        try:
            id = request.GET.get('resid')
        except BaseException:
            return Response({"error_code": 1})
        print(id)
        if id is None:
            return Response({"error_code": 3})
        try: 
            res = Resource.objects.get(resid=id)
        except BaseException:
            return Response({"error_code": 1})
        
        print("ok")
        ResourceTagViewSet.upRes(res)
        res = Resource.objects.get(resid=id)

        serializer = ResourceSerializer(res)
        return Response({
            "error_code": 0,
            "data": serializer.data
        })
    
    def upload(self, request):
        resid = request.data.get('resid')
        name = request.data.get('name')
        desc = request.data.get('description')
        school = request.data.get('school')
        grade = request.data.get('grade')
        tags = request.data.get('tags')
        cost = request.data.get('cost')
        resurl = request.data.get('resurl')
        picurls = request.data.get('picurls')
        uid = request.user.openid

        if school is None:
            school = 'none'
        if grade is None:
            grade = 0
        
        if resid is None:
            try:
                print(resurl)
                print(picurls)
                print(desc)
                ResourceTagViewSet.addStr(tags)
                Resource.objects.create(author=uid,resURL=resurl,picURLs=picurls,
                description=desc,grade=grade,school=school,tags=tags,cost=cost)
            except BaseException as e:
                print(str(e))
                return Response({"error_code": 1})

            obj = Resource.objects.get(resURL=resurl)
            return Response({
                "error_code": 0,
                "data": obj.resid
            })
        else:
            try:
                ResourceTagViewSet.addStr(tags)
                Resource.objects.filter(resid=resid).update(author=uid,resURL=resurl,picURLs=picurls,
                description=desc,grade=grade,school=school,tags=tags,cost=cost)
            except BaseException:
                return Response({"error_code": 1})
            obj = Resource.objects.get(resURL=resurl)
            return Response({
                "error_code": 0,
                "data": obj.resid
            })
        
class ResFolderViewSet(viewsets.ModelViewSet):
    queryset = ResouceFolder.objects.all()
    serializer_class = ResouceFolderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def add(self, request):
        uid=request.user.openid
        print(uid)
        print("xxx")
        rid=request.data.get('resid')
        cmt=request.data.get('comment')
        print(rid)
        if rid is None:
            return Response({"error_code": 3})
        if cmt is None:
            cmt='no comment'
        res = Resource.objects.get(resid=rid)
        if res is None:
            return Response({"error_code": 1})
        if request.user.coin < res.cost:
            return Response({"error_code": 4})
        try:
            ResouceFolder.objects.create(userid=uid,resid=rid,comment=cmt) 
        except BaseException as e:
            print(str(e))
            return Response({"error_code": 1})
        usr = request.user
        usr.coin -= res.cost
        usr.save()
        return Response({"error_code": 0})

    def geturl(self, request):
        uid=request.user.openid
        print("xsadasdsad")
        rid=request.GET.get('resid')
        print(rid)
        if rid is None:
            return Response({"error_code": 3})
        try:
            now = ResouceFolder.objects.get(userid = uid, resid = rid) 
        except BaseException:
            return Response({"error_code": 1})
        if now is not None:
            res = Resource.objects.get(resid = rid)
            serializer = ResourceURLSerializer(res)
            return Response({
                "error_code": 0,
                "data": serializer.data
            })
        else:
            return Response({"error_code": 1})

    def searchfolder(self, request):
        uid = request.user.openid
        res = ResouceFolder.objects.all()
        #少个分页这里 先不写了
        print("xxxxx")
        print(uid)
        print(len(res))
        ser = ResouceFolderSerializer(res, many=True)
        return Response({
        "error_code": 0,
        "data":ser.data
        })
    
    def delfolder(self, request):
        uid = request.user.openid
        rid = request.data.get('resid')
        if rid is None:
            return Response({"error_code": 3})

        res = ResouceFolder.objects.filter(userid=uid, resid=rid)

        if len(res) == 0:
            return Response({"error_code": 1})
        print("tt")

        try:
            ResouceFolder.objects.filter(userid=uid, resid=rid).delete()
        except BaseException:
            return Response({"error_code": 1})

        return Response({"error_code": 0})
        