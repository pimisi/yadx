from rest_framework import generics, permissions
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from .serializers import UserSerializer, PostSerializer, PhotoSerializer, CommentSerializer
from .models import User, Post, Comment, Photo
from .permissions import PostAuthorCanEditPermission

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('api:user-list', request=request, format=format),
        'posts': reverse('api:userpost-list', request=request, format=format)
    })


# User
# class UserViewSet(viewsets.ReadOnlyModeViewSet):
#     """
#     This viewset automatically provides `list` and `detail` actions.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [
#         permissions.AllowAny
#     ]
#
#     # @detail_route(lookup_field = 'username')


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer
    lookup_field = 'username'


class UserPostList(generics.ListAPIView):
    model = Post
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # @override
    def get_queryset(self):
        queryset = super(UserPostList, self).get_queryset()
        return queryset.filter(author__username=self.kwargs.get('username'))


# Posts
class PostMixin(object):
    model = Post
    serializer_class = PostSerializer
    permission_classes = [
        PostAuthorCanEditPermission
    ]

    def pre_save(self, obj):
        """Force author to the current user on save"""
        obj.author = self.request.user
        return super(PostMixin, self).pre_save(obj)


class PostList(PostMixin, generics.ListCreateAPIView):
    pass


class PostDetail(PostMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class PostCommentList(generics.ListAPIView):
    model = Comment
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = super(PostCommentList, self).get_queryset()
        return queryset.filter(post__pk=self.kwargs.get('pk'))


class PostPhotoList(generics.ListAPIView):
    model = Photo
    serializer_class = PhotoSerializer

    def get_queryset(self):
        queryset = super(PostPhotoList, self).get_queryset()
        return queryset.filter(post__pk=self.kwargs.get('pk'))


# Comment
class Comments(generics.ListCreateAPIView):
    pass


class CommentList(generics.ListCreateAPIView):
    model = Comment
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.AllowAny
    ]


# Photo
class PhotoList(generics.ListCreateAPIView):
    model = Photo
    serializer_class = PhotoSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Photo
    serializer_class = PhotoSerializer
    permission_classes = [
        permissions.AllowAny
    ]

