from res.views import ResourceViewSet,ResFolderViewSet
from django.conf.urls import url, include
from rest_framework import routers

urlpatterns = [
    url(r'^search/',ResourceViewSet.as_view({"get":"search"})),
    url(r'^upload/',ResourceViewSet.as_view({"post":"upload"})),
    url(r'^getdetail/',ResourceViewSet.as_view({"get":"details"})),
    url(r'^geturl/',ResFolderViewSet.as_view({"get":"geturl"})),
    url(r'^addfolder/',ResFolderViewSet.as_view({"post":"add"})),
    url(r'^getfolder/',ResFolderViewSet.as_view({"get":"searchfolder"})),
    url(r'^delfolder/',ResFolderViewSet.as_view({"post":"delfolder"})),
]