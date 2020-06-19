from django.contrib import admin
from django.urls import path , include
from .views import ( CommentListView ,CommentCreateView,
	                CommentDetailView ,CommentUpdate)

app_name = "Comment_api"

urlpatterns = [
path('comments/' , CommentListView.as_view(),name='comments'),
path('create/', CommentCreateView.as_view(),name='create'),
path('comments/<pk>',CommentDetailView.as_view(),name='detail'),
path('comments/upd/<pk>',CommentUpdate.as_view(),name='update'),

]