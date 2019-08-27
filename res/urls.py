from res.views import ResourceViewSet
from django.conf.urls import url, include
from rest_framework import routers

urlpatterns = [
    url('search',ResourceViewSet.as_view({"get":"search"})),
    url('get',ResourceViewSet.as_view({"get":"details"})),
]