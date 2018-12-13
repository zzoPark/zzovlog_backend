from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('menus/', views.MenuList.as_view()),
    path('menus/<int:pk>/', views.MenuDetail.as_view()),
    path('tagged/<tagname>', views.TaggedList.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
