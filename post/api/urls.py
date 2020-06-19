
from django.urls import path , include
from .views import (ListView ,DetailView ,UpdateView,
				  DeleteView ,CreateView)
from rest_framework.routers import DefaultRouter

app_name = "Post_api"
router = DefaultRouter()
# router.register('list-view',ListView ,basename='api_list')

urlpatterns = [
path('post/',ListView.as_view(),name='posts'),
path('post/create/',CreateView.as_view(),name='create'),
path('post/<pk>/',DetailView.as_view(),name='detail'),
path('post/del/<pk>/' ,DeleteView.as_view(),name='delete'),
path('post/up/<pk>/',UpdateView.as_view(),name='update'),
path('', include(router.urls))
]