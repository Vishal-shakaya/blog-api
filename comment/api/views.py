from rest_framework.generics import (ListAPIView ,CreateAPIView 
	                            ,RetrieveAPIView ,UpdateAPIView,RetrieveUpdateAPIView)
from rest_framework.mixins import  UpdateModelMixin,DestroyModelMixin
from comment.models import Comment
from .serializer import CommentSerializer ,CommentUpdateSerializer
from comment.models import Comment
from  post.api.pagination import PagePagination
from post.models import post 
from django.shortcuts import get_object_or_404
from rest_framework import mixins 
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import BasicAuthentication


class CommentListView(ListAPIView):
	model = Comment
	serializer_class = CommentSerializer
	queryset = Comment.objects.all()
	pagination_class = PagePagination


class CommentCreateView(CreateAPIView):
	serializer_class = CommentUpdateSerializer
	def perform_create(self , serializer):
		serializer.save(user=self.request.user)



class CommentDetailView(RetrieveAPIView):
	model = Comment
	serializer_class = CommentSerializer
	lookup_field = 'pk'
	queryset = Comment.objects.all()

class CommentUpdate(RetrieveUpdateAPIView ,UpdateModelMixin ,DestroyModelMixin):
	model = Comment 
	serializer_class = CommentUpdateSerializer
	lookup_field = 'pk'
	queryset =Comment.objects.all()
	permission_classes = [IsOwnerOrReadOnly ,IsAuthenticatedOrReadOnly]

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

