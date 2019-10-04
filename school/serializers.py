from rest_framework import serializers
from school.models import School

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = School
        fields = ['code','schoolCode','schoolName','majorName']
    

class SchoolCodeSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = School
        fields = ['schoolCode','schoolName']