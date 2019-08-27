from rest_framework import serializers
from carryu.models import User,Resource,ResouceFolder


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['openid', 'coin', 'school', 'grade']

class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ['resid', 'author', 'resURL', 'school', 'grade', 'picURLs', 'description', 'create_time', 'update_time', 'tags', 'cost']
        
class ResourceListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ['resid', 'name', 'school', 'grade', 'update_time', 'tags', 'cost']        
