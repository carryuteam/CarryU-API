from rest_framework import serializers
from res.models import Resource,ResouceFolder,ResouceTag
from users.models import UserProfile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
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

    def to_representation(self, obj):
        data = super(ResouceFolderSerializer, self).to_representation(obj)
        data['resource'] = ResourceListSerializer(Resource.objects.get(resid=obj.resid)).data
        return data
    
    class Meta:
        model = ResouceFolder
        fields = ['userid', 'resid', 'is_buy', 'comment', 'add_time']

class ResourceURLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ['resid', 'resURL'] 

class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ResouceTag
        fields = ['tag'] 
        
