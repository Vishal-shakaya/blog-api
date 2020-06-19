
from django.urls import path , include
from .views import CreateView


app_name = "User_api"

urlpatterns = [
path('register/',CreateView.as_view(),name='register'),
]