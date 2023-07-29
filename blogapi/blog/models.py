from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
	created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length = 100)
	description = models.TextField()
	content = models.TextField()
	create_date_time = models.DateTimeField(auto_now_add=True,null=True)
	updated_date_time = models.DateTimeField(auto_now=True,null=True)
	is_private= models.BooleanField(default=False)

	class Meta:
		ordering = ['create_date_time']

	def __str__(self):
		return self.title

class LikeBlog(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

	class Meta:
		unique_together = ['blog','user']

