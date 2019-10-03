from res.views import ResourceViewSet,ResFolderViewSet
from res.tags import ResourceTagViewSet
from django.conf.urls import url, include
from rest_framework import routers

urlpatterns = [
    url(r'^search/',ResourceViewSet.as_view({"get":"search"})),
    url(r'^update/',ResourceViewSet.as_view({"post":"update"})),
    url(r'^delres/',ResourceViewSet.as_view({"post":"delRes"})),
    url(r'^getdetail/',ResourceViewSet.as_view({"get":"details"})),
    url(r'^refresh/',ResourceViewSet.as_view({"post":"refresh"})),
    url(r'^geturl/',ResFolderViewSet.as_view({"get":"geturl"})),
    url(r'^addbuy/',ResFolderViewSet.as_view({"post":"add_and_buy"})),

    url(r'^folder/add/',ResFolderViewSet.as_view({"post":"add"})),
    url(r'^folder/get/',ResFolderViewSet.as_view({"get":"getfolder"})),
    url(r'^folder/del/',ResFolderViewSet.as_view({"post":"delfolder"})),
    url(r'^folder/buy/',ResFolderViewSet.as_view({"post":"buy"})),


    url(r'^tag/add/',ResourceTagViewSet.as_view({"post":"addTag"})),
    url(r'^tag/del/',ResourceTagViewSet.as_view({"post":"delTag"})),
    url(r'^tag/get/',ResourceTagViewSet.as_view({"get":"getTag"})),
    url(r'^tag/search/',ResourceTagViewSet.as_view({"get":"searchTag"})),
]