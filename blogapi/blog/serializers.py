from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog, LikeBlog
from django.db.models import Count

class LikeSerializer(serializers.ModelSerializer):
	class Meta:
		model = LikeBlog
		fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
	total_like = serializers.SerializerMethodField(read_only=True)
	
	def get_total_like(self, blog):
		return blog.likeblog_set.count()

	class Meta:
		model = Blog
		fields = ['created_by','is_private','title','description','content','create_date_time','updated_date_time','total_like']


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'


