from rest_framework.permissions import BasePermission

class CanAccessBlogPermission(BasePermission):

	def has_object_permission(self, request, view, obj):
		if request.method in ['GET','POST', 'HEAD', 'OPTIONS']:
			return True
		#if created_by user same as requested user
		return obj.created_by == request.user
