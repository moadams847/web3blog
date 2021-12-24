from django.urls import path
from . import views

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CategoryListView
  )

urlpatterns = [
  
  path('', PostListView.as_view(), name='blog-home'),
  path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
  path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
  path('category/<str:name>/', CategoryListView.as_view(), name='category-posts'),
  path('post/<int:pk>/add_comment/', views.add_comment, name='add-comment'),
  path('post/new/', PostCreateView.as_view(), name='post-create'),
  path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
  path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]
