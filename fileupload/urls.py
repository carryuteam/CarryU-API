from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', UploadViewSet.as_view({'post': 'post'})),
    path('download/<int:fid>', UploadViewSet.as_view({'get': 'get'})),
]
