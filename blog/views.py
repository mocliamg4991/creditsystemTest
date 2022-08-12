from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# Create your views here.
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.http import HttpResponseNotFound
from .models import Post
import json


class PostListView(ListView):

    model = Post
    template_name = 'blog/index.html'
    paginate_by = 2
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name='blog/post-detail.html'
 
 
class PostCreateView(CreateView):
    model = Post
    fields = ['slug', 'title', 'description', 'available']
    template_name = 'blog/post-add.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['slug', 'title', 'description', 'available']

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('posts_list')
