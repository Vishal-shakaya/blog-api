from rest_framework.generics import (ListAPIView ,RetrieveAPIView,
DestroyAPIView ,UpdateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView )

from rest_framework.filters import SearchFilter ,OrderingFilter									
from post.models import post
from .pagination import LimitPagination , PagePagination
from .serializers import PostSerializer , CreateUpdateSerializer





class CreateView(CreateAPIView):
	serializer_class =  CreateUpdateSerializer
	queryset = post.objects.all()

	def perform_create(self , serializer):
		serializer.save(user=self.request.user)

class ListView(ListAPIView):
	queryset = post.objects.all()
	serializer_class =PostSerializer
	filter_backends = [SearchFilter,OrderingFilter]
	# ordering_fields=['title','id']
	# search_fields = ['title','content']
	# pagination_class = PagePagination


class DetailView(RetrieveAPIView):
	serializer_class =PostSerializer
	queryset = post.objects.all()
	lookup_field= 'pk'


class UpdateView(RetrieveUpdateDestroyAPIView):
	serializer_class = CreateUpdateSerializer
	queryset = post.objects.all()
	lookup_field= 'pk'

	def perform_update(self , serializer):
		serializer.save(user=self.request.user)



class DeleteView(DestroyAPIView):
	serializer_class =PostSerializer
	queryset = post.objects.all()
	lookup_field= 'pk'
