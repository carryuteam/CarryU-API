#!coding=utf-8
from .models import *
from rest_framework import serializers


class ShareSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['uid'] = self.context['user'].openid
        return ShareModel.objects.create(**validated_data)

    class Meta:
        model = ShareModel
        fields = ['title', 'content']


class ShareCommentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['uid'] = self.context['user'].openid
        comment = ShareComment.objects.create(**validated_data)
        share = ShareModel.objects.filter(id=comment.sid)[0]
        if share:
            share.comment += 1
            share.save()
            return comment
        return None

    class Meta:
        model = ShareComment
        fields = ['sid', 'comment']


class ShareLikeSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['uid'] = self.context['user'].openid
        like = ShareLike.objects.create(**validated_data)
        share = ShareModel.objects.filter(id=like.sid)[0]

        if share:
            share.like += 1
            share.save()
            return like
        return None

    class Meta:
        model = ShareLike
        fields = ['sid']


class ShareStoreSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['uid'] = self.context['user'].openid
        store = ShareStore.objects.create(**validated_data)
        share = ShareModel.objects.filter(id=store.sid)[0]
        if share:
            share.store += 1
            share.save()
            return store
        return None

    class Meta:
        model = ShareLike
        fields = ['sid']


class ShareOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareModel
        fields = '__all__'


class ShareCommentOutSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShareComment
        fields = '__all__'


class ShareLikeOutSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShareLike
        fields = '__all__'


class ShareStoreOutSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShareStore
        fields = '__all__'

