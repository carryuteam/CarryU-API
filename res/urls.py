from res.views import ResourceViewSet,ResFolderViewSet
from django.conf.urls import url, include
from rest_framework import routers

urlpatterns = [
    url('search',ResourceViewSet.as_view({"get":"search"})),
    url('upload',ResourceViewSet.as_view({"post":"upload"})),
    url('get',ResourceViewSet.as_view({"get":"details"})),
    url('takeurl',ResFolderViewSet.as_view({"get":"geturl"})),
    url('add',ResFolderViewSet.as_view({"post":"add"})),
]