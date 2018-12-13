from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics, filters
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from blog.models import Tag, Post, Menu
from blog.serializers import UserSerializer, GroupSerializer, TagSerializer, PostSerializer, MenuSerializer


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
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'contents',)

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)


class TaggedList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        tagname = self.kwargs['tagname']
        tag = Tag.objects.get(name=tagname)
        posts = Post.objects.filter(id__in=tag.posts.all())
        return posts


class MenuList(APIView):
    def get(self, request, format=None):
        menus = Tag.objects.filter(id__in=Menu.objects.all().values('tag'))
        serializer = TagSerializer(menus, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
