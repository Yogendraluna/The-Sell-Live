from django.urls import path
from .views import (
    PostCreateView,
    PostListView,
    PostUpdateView,
    PostDetailView,
    PostDeleteView,
)

urlpatterns = [
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('<pk>/edit/',PostUpdateView.as_view(), name='post_edit'),
    path('<pk>/',PostDetailView.as_view(), name='post_detail'),
    path('<pk>/delete/',PostDeleteView.as_view(), name='post_delete'),
    path('', PostListView.as_view(), name='post_list'),
]
