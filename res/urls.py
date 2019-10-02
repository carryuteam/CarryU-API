from res.views import ResourceViewSet,ResFolderViewSet
from res.tags import ResourceTagViewSet
from django.conf.urls import url, include
from rest_framework import routers

urlpatterns = [
    url(r'^search/',ResourceViewSet.as_view({"get":"search"})),
    url(r'^update/',ResourceViewSet.as_view({"post":"update"})),
    url(r'^getdetail/',ResourceViewSet.as_view({"get":"details"})),
    url(r'^refresh/',ResourceViewSet.as_view({"post":"refresh"})),
    url(r'^geturl/',ResFolderViewSet.as_view({"get":"geturl"})),
    url(r'^addfolder/',ResFolderViewSet.as_view({"post":"add"})),
    url(r'^getfolder/',ResFolderViewSet.as_view({"get":"searchfolder"})),
    url(r'^delfolder/',ResFolderViewSet.as_view({"post":"delfolder"})),
    url(r'^addtag/',ResourceTagViewSet.as_view({"post":"addTag"})),
    url(r'^gettag/',ResourceTagViewSet.as_view({"get":"getTag"})),
    url(r'^searchtag/',ResourceTagViewSet.as_view({"get":"searchTag"})),
]