from school.views import SchoolViewSet,AdminSchoolViewSet
from django.conf.urls import url, include
from rest_framework import routers

urlpatterns = [
    url(r'^get/$',SchoolViewSet.as_view({"get":"get"})),
    url(r'^add/$',AdminSchoolViewSet.as_view({"post":"add"})),
    url(r'^getall/$',SchoolViewSet.as_view({"get":"getAll"})),
    url(r'^getschool/$',SchoolViewSet.as_view({"get":"getSchool"})),
]
