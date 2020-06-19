from rest_framework import serializers  
from rest_framework.serializers import HyperlinkedIdentityField ,SerializerMethodField
from post.models import post
from api.serializers import UserDetailSerializer
from comment.api.serializer import CommentSerializer
from comment.models import Comment

class PostSerializer(serializers.ModelSerializer):
	url = HyperlinkedIdentityField(view_name='Post_api:detail', )
	user = UserDetailSerializer()
	image = SerializerMethodField()

	class Meta:
	    model = post
	    fields = ['user','image','title', 'content', 'publish','url']

	# def get_user(self, obj):
	# 	return str(obj.user.username+'  ''feelsafe user')

	def get_image(self, obj):
		if obj.image:
			return obj.image.url
		else:
			return ''
		# try:
		# 	obj.image.url
		# except:
		# 	obj.image=None
		# return obj.image.url

class CreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ['title', 'content', 'publish']
