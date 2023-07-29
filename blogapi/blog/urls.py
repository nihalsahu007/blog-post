from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'post-blog',BlogView)
router.register(r'like-blog',LikeBlogView)
router.register(r'user',UserView)


urlpatterns = [
	path('', include(router.urls)),
]