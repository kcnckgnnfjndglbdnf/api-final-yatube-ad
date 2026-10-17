from django.urls import include, path
from rest_framework.routers import DefaultRouter

from posts.views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostViewSet,
)

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register('follow', FollowViewSet, basename='follow')

comment_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
comment_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('posts/<int:post_id>/comments/', comment_list),
    path('posts/<int:post_id>/comments/<int:pk>/', comment_detail),
    path('', include(router.urls)),
]
