from carryu_file.views import ResourceViewSet
from django.conf.urls import url, include
from rest_framework import routers

urlpatterns = [
    url('search',ResourceViewSet.as_view({"get":"search"}))
]