from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blog.models import Tag, Post, Menu


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups', 'posts')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class TagSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all(), required=False)
    class Meta:
        model = Tag
        fields = ('id', 'name', 'posts')


class PostSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')
    class Meta:
        model = Post
        fields = ('id', 'title', 'contents', 'write_date', 'update_date', 'writer', 'tags')
        extra_kwargs = { 'tags': { 'required': False } }


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'tag')
