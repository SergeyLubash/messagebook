from rest_framework import routers

from .views import UsersViewSet, PostsViewSet, CommentsViewSet

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'posts', PostsViewSet)
router.register(r'comments', CommentsViewSet)
