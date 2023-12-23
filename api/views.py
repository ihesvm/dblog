from django.shortcuts import render
from posts.models import Post
from django.http import JsonResponse
from django.core import serializers
# Create your views here.


@login_required
def all_posts(request):
    posts = Post.objects.all()
    data = serializers.serialize('json', posts)
    return JsonResponse(data, safe=False)






