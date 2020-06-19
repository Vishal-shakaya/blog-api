from .serializers import RegisterSerializer,UserDetailSerializer
from rest_framework.generics import CreateAPIView , RetrieveAPIView ,ListAPIView
from django.contrib.auth import get_user_model
User = get_user_model()
class CreateView(CreateAPIView):
	serializer_class = RegisterSerializer
