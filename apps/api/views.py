from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.api.models import User, Post, Comment
from apps.api.permissions import IsOwnerOrReadOnly
from apps.api.serializers import UserSerializer, PostSerializer, CommentSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.reverse import reverse
from django.core.mail import send_mail
from django.core.mail import EmailMessage


@csrf_exempt
@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('api:user-list', request=request, format=format),
        'posts': reverse('api:post-list', request=request, format=format)
    })


class Contact(APIView):
    def post(self, request, *args, **kwargs):
        print("Request")
        print(self.request.data)
        print(type(self.request.data))
        # Get the data out
        request_data = self.request.data
        print(request_data["subject"])
        # Send the mail

        mail = EmailMessage(
            subject='%s from %s' % (request_data["subject"], request_data["firstname"]),
            body=request_data["message"],
            from_email=request_data["email"],
            to=["info@yadxdigital.com"]
        )

        mail.send()
        # send_mail(
        #     '%s from %s' % (request_data["subject"], request_data["firstname"]),
        #     request_data["message"],
        #     request_data["email"],
        #     ['paul.imisi@gmail.com'],
        #     fail_silently=False)

        return Response({"message": "The email has been sent"})


class CommentList(generics.ListCreateAPIView):
    model = Comment
    serializer_class = CommentSerializer
    # permission_classes = [
    #     permissions.AllowAny
    # ]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)


class PostList(generics.ListCreateAPIView):
    """
    List all posts, or create a new post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

        # def get(self, request, format=None):
        #     posts = Post.objects.all()
        #     serializer = PostSerializer(posts, many=True)
        #     return Response(serializer.data)
        #
        # def post(self, request, format=None):
        #     serializer = PostSerializer(data=request.data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a post.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)

    # def get_object(self, pk):
    #     try:
    #         return Post.objects.get(pk=pk)
    #     except Post.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, pk, format=None):
    #     post = self.get_object(pk)
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk, format=None):
    #     post = self.get_object(pk)
    #     serializer = PostSerializer(post, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(post.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     post = self.get_object(pk)
    #     post.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    #
    # @csrf_exempt
    # @api_view(['GET', 'POST'])
    # def post_list(request, format=None):
    #     """
    #     List all posts, or create a new post.
    #     """
    #     if request.method == 'GET':
    #         posts = Post.objects.all()
    #         serializer = PostSerializer(posts, many=True)
    #         return JSONResponse(serializer.data)
    #
    #     elif request.method == 'POST':
    #         data = JSONParser().parse(request)
    #         serializer = PostSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JSONResponse(serializer.data, status=201)
    #         return JSONResponse(serializer.errors, status=400)
    #
    # @csrf_exempt
    # @api_view(['GET', 'PUT', 'DELETE'])
    # def post_detail(request, pk, format=None):
    #     """
    #     Retrieve, update or delete a post.
    #     """
    #     try:
    #         post = Post.objects.get(pk=pk)
    #     except Post.DoesNotExist:
    #         return HttpResponse(status=404)
    #
    #     if request.method == 'GET':
    #         serializer = PostSerializer(post)
    #         return JSONResponse(serializer.data)
    #
    #     elif request.method == 'PUT':
    #         data = JSONParser().parse(request)
    #         serializer = PostSerializer(post, data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JSONResponse(serializer.data)
    #         return JSONResponse(serializer.errors, status=400)
    #
    #     elif request.method == 'DELETE':
    #         post.delete()
    #         return HttpResponse(status=204)



