from rest_framework import serializers  
from rest_framework.serializers import HyperlinkedIdentityField ,SerializerMethodField
from comment.models import Comment
from post.models import post
from api.serializers import UserDetailSerializer
	
class CommentSerializer(serializers.ModelSerializer):
	# update = HyperlinkedIdentityField(view_name='Comment_api:update')
	user = UserDetailSerializer()
	class Meta:
	    model = Comment
	    fields = ['id','user', 'content','date' ,'post']



class CommentUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		user = UserDetailSerializer()
		model = Comment
		fields = ['user','post','content']	    

