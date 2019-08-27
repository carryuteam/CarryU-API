from rest_framework import serializers
from res.models import User,Resource,ResouceFolder


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['openid', 'coin', 'school', 'grade']

class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ['resid', 'name', 'author', 'school', 'grade', 'picURLs', 'description', 'create_time', 'update_time', 'tags', 'cost']
        
class ResourceListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ['resid', 'name', 'author', 'school', 'grade', 'update_time', 'tags', 'cost'] 

class ResouceFolderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ResouceFolder
        fields = ['userid', 'resid']
