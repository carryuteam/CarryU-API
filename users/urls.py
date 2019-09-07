from django.conf.urls import url
from .views import *

urlpatterns = [
    url('login', UserViewSet.as_view({'post': 'list'})),
    url('register', UserViewSet.as_view({'post': 'create'})),
    url('update', UserUpdateViewSet.as_view({'post': 'update'})),
    url('getdetail', UserUpdateViewSet.as_view({'get': 'getdetail'})),    
    url('addcoin', UserUpdateViewSet.as_view({'post': 'addcoin'})),    
]
