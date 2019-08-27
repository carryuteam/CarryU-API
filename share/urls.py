from django.urls import path
from .views import *

urlpatterns = [
    path('<int:sid>/', ShareViewSet.as_view({'get': 'retrieve'})),
    path('publish', ShareViewSet.as_view({'post': 'create'})),
    path('', ShareViewSet.as_view({'get': 'list'})),

    path('comment', ShareCommentViewSet.as_view({'post': 'create'})),
    path('<int:sid>/comment/', ShareCommentViewSet.as_view({'get': 'list'})),
    path('comment/<int:cid>/', ShareCommentViewSet.as_view({'get': 'retrieve'})),

    path('like', ShareLikeViewSet.as_view({'post': 'create'})),
    path('<int:sid>/like/', ShareLikeViewSet.as_view({'get': 'list'})),
    path('like/<int:lid>/', ShareLikeViewSet.as_view({'get': 'retrieve'})),

    path('store', ShareStoreViewSet.as_view({'post': 'create'})),
    path('<int:sid>/store/', ShareStoreViewSet.as_view({'get': 'list'})),
    path('store/<int:lid>/', ShareStoreViewSet.as_view({'get': 'retrieve'})),
]
