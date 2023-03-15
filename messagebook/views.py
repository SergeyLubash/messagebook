from rest_framework import viewsets
from messagebook.permissions import PermissionPolicyMixin, IsOwner
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from messagebook.models import Users, Posts, Comments
from messagebook.serializers import UsersSerializer, PostsSerializer, CommentsSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes_per_method = {
        'list': [IsAdminUser, IsAuthenticated],
        'create': [AllowAny],
        'update': [IsAdminUser, IsOwner],
        'destroy': [IsAdminUser],
    }


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes_per_method = {
        'list': [AllowAny],
        'create': [IsAuthenticated],
        'update': [IsAdminUser, IsOwner],
        'destroy': [IsAdminUser, IsOwner],
    }


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes_per_method = {
        'list': [AllowAny],
        'create': [IsAuthenticated],
        'update': [IsAdminUser, IsOwner],
        'destroy': [IsAdminUser, IsOwner],
    }

# docker run --name message_db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres