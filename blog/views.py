from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics, filters
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from blog.models import Tag, Post, Menu
from blog.serializers import UserSerializer, GroupSerializer, TagSerializer, PostSerializer, MenuSerializer

import logging

logger = logging.getLogger(__name__)


class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('last_used')
    serializer_class = TagSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-update_date')
    serializer_class = PostSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'contents',)

    def create(self, request, *args, **kwargs):
        post = request.data
        tagnames = []
        for name in post['tags'].split(','):
            if not name.strip(): continue
            tag, created = Tag.objects.update_or_create(name=name)
            tagnames.append(tag.name)
        post['tags'] = tagnames
        serializer = self.get_serializer(data=post)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)


class TaggedList(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-update_date')
    serializer_class = PostSerializer

    def get_queryset(self):
        tagname = self.kwargs['tagname']
        tag = Tag.objects.get(name=tagname)
        posts = self.queryset.filter(id__in=tag.posts.all())
        return posts


class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all().order_by('order')
    serializer_class = MenuSerializer

    def create(self, request, *args, **kwargs):
        menus = request.data
        logger.info(menus)
        Menu.objects.all().delete()
        for menu in menus:
            logger.info(menu)
            serializer = self.get_serializer(data=menu)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
