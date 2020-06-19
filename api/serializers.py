from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username' ,'email', 'password']

    def create(self , validate_data):
    	username = validate_data['username']
    	email = validate_data['email']
    	password = validate_data['password']
    	user = User(username=username, email=email)
    	user.set_password(password)
    	user.save()
    	return validate_data


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk','username' ,'email',]    