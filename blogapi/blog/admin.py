from django.contrib import admin
from .models import Blog, LikeBlog

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	search_fields = ("title",)
	list_display = ['created_by','title','description','content','create_date_time','updated_date_time']

# admin.site.register(Blog)

@admin.register(LikeBlog)
class LikeBlogAdmin(admin.ModelAdmin):
	search_fields = ("blog__created_by",)
	list_display = [field.name for field in LikeBlog._meta.get_fields()]