from typing import Any

from django.contrib import messages
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from posts.forms import PostForm
from posts.models import Post
from django.views.generic import ListView, DetailView


# Create your views here.

# def all_posts(request):
#     posts = Post.postM.just_published()
#
#     return render(request, 'posts/all_posts.html', {'posts': posts})


# def all_posts(request):
#     posts = Post.posts.published()
#
#     return render(request, 'posts/all_posts.html', {'posts': posts})
#

class PostListView(ListView):
    model = Post
    queryset = Post.posts.published()
    template_name = 'posts/all_posts.html'


# def get_posts(request, slug):
#     # post = get_object_or_404(Post, slug=slug)
#
#     post = Post.postM.slugs(slug)
#     # post = Post.objects.get(slug=slug)
#
#     return render(request, 'posts/get_posts.html', {'post': post})


# def post_form(request):
#     form = PostForm()
#
#     return render(request, 'posts/posts_form.html', {'form': form})


class PostDetail(DetailView):
    model = Post
    template_name = 'posts/get_posts.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(slug=slug)


# def save_form(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#
#     return redirect('posts-form')


# def get_posts(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, 'posts/get_posts.html', {'post': post})

#
# def post_save(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#
#     return redirect('posts-form')


class PostView(View):
    __form = PostForm

    def get(self, request):
        return render(request, 'posts/posts_form.html', {'form': self.__form()})

    def post(self, request):
        if request.method == 'POST':
            form = self.__form(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Post Created !!!')
                return redirect('home:home')

        messages.warning(request, 'Post Error !!!')
        return redirect('posts:posts-form')
