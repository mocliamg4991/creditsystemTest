from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView


urlpatterns = [

    path('', PostListView.as_view(), name='posts_list'),
    path('post/add/', PostCreateView.as_view(), name='post_add'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/update/<slug:slug>/', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<slug:slug>/', PostDeleteView.as_view(), name='post_delete'),
    
]
