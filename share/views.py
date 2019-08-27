from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import *
from rest_framework.response import Response


class ShareViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = ShareSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            share = serializer.save()
            ret = {
                "error_code": 0,
                "id": share.id
            }
            return Response(ret)
        return Response({
            "error_code": 500,
            "error": serializer.errors
        })

    def retrieve(self, request, sid):
        share = ShareModel.objects.filter(id=sid)[0]
        ret = {
            "error_code": 0,
            "data": ShareOutSerializer(share).data
        }
        return Response(ret)

    def list(self, request):
        pagesize = request.GET.get('pagesize', default=5)
        page = request.GET.get('page', default=0)
        shares = ShareModel.objects.all()
        paginator = Paginator(shares, pagesize)
        total = paginator.count

        try:
            res = paginator.page(page)
        except PageNotAnInteger:
            res = paginator.page(1)
        except EmptyPage:
            res = paginator.page(paginator.num_pages)

        ret = {
            "error_code": 0,
            "data": ShareOutSerializer(res, many=True).data,
            "total": total
        }
        return Response(ret)


class ShareCommentViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = ShareCommentSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            comment = serializer.save()
            ret = {
                "error_code": 0,
                "data": comment.id
            }
            return Response(ret)
        return Response({
            "error_code": 500,
            "error": serializer.errors
        })

    def list(self, request, sid):
        pagesize = request.GET.get('pagesize', default=5)
        page = request.GET.get('page', default=0)
        comments = ShareComment.objects.filter(sid=sid)
        paginator = Paginator(comments, pagesize)
        total = paginator.count

        try:
            res = paginator.page(page)
        except PageNotAnInteger:
            res = paginator.page(1)
        except EmptyPage:
            res = paginator.page(paginator.num_pages)

        ret = {
            "error_code": 0,
            "data": ShareCommentOutSerializer(res, many=True).data,
            "total": total
        }
        return Response(ret)

    def retrieve(self, request, cid):
        comment = ShareComment.objects.filter(id=cid)[0]
        ret = {
            "error_code": 0,
            "data": ShareCommentOutSerializer(comment).data
        }
        return Response(ret)


class ShareLikeViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = ShareLikeSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            like = serializer.save()
            ret = {
                "error_code": 0,
                "id": like.id
            }
            return Response(ret)
        return Response({
            "error_code": 500,
            "error": serializer.errors
        })

    def list(self, request, sid):
        pagesize = request.GET.get('pagesize', default=5)
        page = request.GET.get('page', default=0)
        like = ShareLike.objects.filter(sid=sid)
        paginator = Paginator(like, pagesize)
        total = paginator.count

        try:
            res = paginator.page(page)
        except PageNotAnInteger:
            res = paginator.page(1)
        except EmptyPage:
            res = paginator.page(paginator.num_pages)

        ret = {
            "error_code": 0,
            "data": ShareLikeOutSerializer(res, many=True).data,
            "total": total
        }
        return Response(ret)

    def retrieve(self, request, lid):
        comment = ShareLike.objects.filter(id=lid)[0]
        ret = {
            "error_code": 0,
            "data": ShareLikeOutSerializer(comment).data
        }
        return Response(ret)


class ShareStoreViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = ShareStoreSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            store = serializer.save()
            ret = {
                "error_code": 0,
                "id": store.id
            }
            return Response(ret)
        return Response({
            "error_code": 500,
            "error": serializer.errors
        })

    def list(self, request, sid):
        pagesize = request.GET.get('pagesize', default=5)
        page = request.GET.get('page', default=0)
        store = ShareStore.objects.filter(sid=sid)
        paginator = Paginator(store, pagesize)
        total = paginator.count

        try:
            res = paginator.page(page)
        except PageNotAnInteger:
            res = paginator.page(1)
        except EmptyPage:
            res = paginator.page(paginator.num_pages)

        ret = {
            "error_code": 0,
            "data": ShareStoreOutSerializer(res, many=True).data,
            "total": total
        }
        return Response(ret)

    def retrieve(self, request, lid):
        comment = ShareStore.objects.filter(id=lid)[0]
        ret = {
            "error_code": 0,
            "data": ShareStoreOutSerializer(comment).data
        }
        return Response(ret)

