from django.shortcuts import get_object_or_404, render
from home.models import Contact
from home.serializers import ContactSerializer
from posts.models import Post
from django.http import JsonResponse
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from posts.serializers import PostSerializer
from rest_framework import status

# Create your views here.



def all_posts(request):
    posts = Post.objects.all()
    data = serializers.serialize('json', posts)
    return JsonResponse(data, safe=False)


@api_view(['GET'])
def posts_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)


    if request.method == 'GET':
        serializer = PostSerializer(posts)
        return Response(serializer.data)




@api_view(['GET', 'POST'])
def contact_list(request):

    if request.method == 'GET':
        contact = Contact.objects.all()
        seria = ContactSerializer(contact, many=True)
        return Response(seria.data)
    

    if request.method == 'POST':
        serialiazer = ContactSerializer(data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response(serialiazer.data, status=status.HTTP_201_CREATED)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)