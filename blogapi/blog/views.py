from django.shortcuts import render
from .serializers import *
from .models import Blog, LikeBlog
from rest_framework import viewsets
from blog.permissions import CanAccessBlogPermission
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

# Create your views here.

class BlogView(viewsets.ModelViewSet):

	queryset = Blog.objects.all()
	serializer_class = BlogSerializer
	permission_classes = [CanAccessBlogPermission]
	
	def get_queryset(self):
		if self.request.user.is_authenticated:
			queryset = self.queryset.filter(created_by=self.request.user)
		else:
			queryset = self.queryset.filter(is_private=False)
		return queryset
		
class LikeBlogView(viewsets.ModelViewSet):
	
	queryset = LikeBlog.objects.filter()
	serializer_class = LikeSerializer

class UserView(viewsets.ModelViewSet):

	queryset = User.objects.all() 
	serializer_class = UserSerializer	
