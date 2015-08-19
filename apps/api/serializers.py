from collections import OrderedDict
from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField
from apps.api.models import User, Photo, Post, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedIdentityField(
        view_name='api:userpost-list', lookup_field='username',
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'posts')



class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(required=False)
    slug = serializers.CharField(required=False)
    comments = serializers.HyperlinkedIdentityField(view_name='api:postcomment-list')
    # url = serializers.HyperlinkedIdentityField(view_name='api:post-detail')
    # url = serializers.CharField(source='get_absolute_url', read_only=True)
    # photos = serializers.HyperlinkedIdentityField(view_name='api:postphoto-list')

    def get_validation_exclusions(self):
        # Need to exclude `author` since we'll add that later based off the request
        exclusions = super(PostSerializer, self).get_validation_exclusions()
        return exclusions + ['author']

    def get_fields(self):
        fields = super(PostSerializer, self).get_fields()
        modified_fields = OrderedDict([('self', HyperlinkedIdentityField(view_name='api:post-detail')) if k == 'url'
                                       else (k, v) for k, v in fields.items()])
        return modified_fields

    class Meta:
        model = Post
        # fields = ('id', 'title', 'content', 'author', 'slug', 'created_date')


class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.Field(source='image.url')

    class Meta:
        model = Photo


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)  # May be an anonymous user.
    content = serializers.CharField(max_length=200)
    created_date = serializers.DateTimeField()

    class Meta:
        model = Comment
