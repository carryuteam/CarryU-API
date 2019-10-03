from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from res.models import ResouceTag,Resource,ResouceComment
from res.serializers import CommentSerializer
from django.db import models
from django.db.models import Avg

class ResourceCommentViewSet(viewsets.ModelViewSet):
    queryset = ResouceComment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def calcScore(resid):
        baseScore=4.5
        offset=0.5
        total=ResouceComment.objects.filter(resid=resid).count()
        avgScore=ResouceComment.objects.filter(resid=resid).aggregate(Avg('score'))
        if total>=10:
            return avgScore['score__avg']
        #left+right=10
        right=10-total
        left=10-right
        left+=offset
        right-=offset
        left=left*0.1
        right=right*0.1
        score=avgScore['score__avg']*left+baseScore*right
        return '%.1f' % score

    def get(self, request):
        search_dict = dict()
        uid=request.GET.get('openid')
        resid=request.GET.get('resid')
        id=request.GET.get('id')

        if uid is None:
            uid=request.user.openid
        search_dict['userid']=uid
        if resid:
            search_dict['resid']=resid
        if id:
            search_dict['id']=id
         
        res=ResouceComment.objects.filter(**search_dict)
        ser=CommentSerializer(res, many=True)
        return Response({
        "error_code": 0,
        "data":ser.data
        })

    def add(self, request):
        resid=request.data.get('resid')
        comment=request.data.get('comment')
        score=request.data.get('score')
        uid=request.user.openid
        if resid is None or score is None:
            return Response({"error_code": 3})
        if comment is None:
            comment="无评论"
        try:
            res=Resource.objects.get(resid=resid)
        except BaseException:
            return Response({"error_code": 1})      
        ResouceComment.objects.create(resid=resid,userid=uid,content=comment,score=score)
        res.score=ResourceCommentViewSet.calcScore(resid)
        res.save()
        return Response({"error_code": 0}) 

    def upRes(res):
        res.score=ResourceCommentViewSet.calcScore(res.resid)
        res.save()



    

