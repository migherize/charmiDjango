from django.urls import path
from . import views

urlpatterns = [
	path('',views.post_list,name='post_list'),
	path('Profile/new', views.profile_new, name='profile_new'),
]