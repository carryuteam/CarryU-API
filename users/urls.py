from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login', UserViewSet.as_view({'post': 'list'})),
    url(r'^register', UserViewSet.as_view({'post': 'create'})),
    url(r'^update', UserUpdateViewSet.as_view({'post': 'update'})),
    url(r'^getdetail', UserUpdateViewSet.as_view({'get': 'getdetail'})),    
    url(r'^addcoin', UserUpdateViewSet.as_view({'post': 'addcoin'})),    
]
