from typing import Any

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response

from posts.forms import PostForm
from posts.models import Post
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from posts.serializers import PostSerializer


# Create your views here.

# def all_posts(request):
#     posts = Post.postM.just_published()
#
#     return render(request, 'posts/all_posts.html', {'posts': posts})

# @login_required
# def all_posts(request):
#     posts = Post.posts.published()
#
#     return render(request, 'posts/all_posts.html', {'posts': posts})
#


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
    slug_url_kwarg = 'slug'



    # def get_queryset(self):
    #     slug = self.kwargs['slug']
    #     return Post.objects.filter(slug=slug)


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


class PostView(LoginRequiredMixin, View):
    __form = PostForm

    def get(self, request):
        return render(request, 'posts/posts_form.html', {'form': self.__form()})

    def post(self, request):
        if request.method == 'POST':
            form = self.__form(request.POST, request.FILES)
            if form.is_valid():
                form.instance.author = request.user
                form.save()
                messages.success(request, 'Post Created !!!')
                return redirect('home:home')

        messages.warning(request, 'Post Error !!!')
        return redirect('posts:posts-form')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy('home:home')
    template_name = 'posts/posts_form.html'
    fields = ['title', 'body', 'publish', 'image', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post Created !!!')
        return super().form_valid(form)



class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home:home')
    slug_url_kwarg = 'slug'

    template_name = 'posts/confirm_delete.html'

    def form_valid(self, form):
        messages.success(self.request, 'Post Deleted!!!')
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'body', 'publish', 'image', 'category']
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('home:home')
    template_name = 'posts/update_post.html'

    def form_valid(self, form):
        messages.success(self.request, 'Post Updated!!!')
        return super().form_valid(form)

