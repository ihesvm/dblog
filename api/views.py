from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView

from home.models import Contact
from home.serializers import ContactSerializer
from posts.models import Post
from django.http import JsonResponse, Http404
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from posts.serializers import PostSerializer
from rest_framework import status, mixins, generics


# Create your views here.


# def all_posts(request):
#     posts = Post.objects.all()
#     data = serializers.serialize('json', posts)
#     return JsonResponse(data, safe=False)


# @api_view(['GET'])
# def posts_list(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#
# @api_view(['GET'])
# def post_detail(request, pk):
#     posts = get_object_or_404(Post, pk=pk)
#
#     if request.method == 'GET':
#         serializer = PostSerializer(posts)
#         return Response(serializer.data)
#
#
# @api_view(['GET', 'POST'])
# def contact_view(request):
#     if request.method == 'GET':
#         contact = Contact.objects.all()
#         seria = ContactSerializer(contact, many=True)
#         return Response(seria.data)
#
#     if request.method == 'POST':
#         serialiazer = ContactSerializer(data=request.data)
#         if serialiazer.is_valid():
#             serialiazer.save()
#             return Response(serialiazer.data, status=status.HTTP_201_CREATED)
#         return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ContactView(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Contact.objects.get(pk=pk)
#         except Contact.DoesNotExist:
#             raise Http404("Contact does not exist")
#
#     def get(self, request, pk):
#         contact = self.get_object(pk=pk)
#         serializer = ContactSerializer(contact)
#         return Response(serializer.data)
#
#     def delete(self, request, pk):
#         contact = self.get_object(pk=pk)
#         contact.delete()
#         return JsonResponse({"message": "Contact Deleted"}, safe=False)
#
#     def post(self, request):
#         serializer = ContactSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk):
#         contact = self.get_object(pk=pk)
#         serializer = ContactSerializer(contact, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactApiView(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)




class PostApiDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer




class PostApiView(APIView):


    def get(self, request):
        posts = Post.posts.published()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
