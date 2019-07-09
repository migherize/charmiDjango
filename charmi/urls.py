from django.urls import path
from . import views

urlpatterns = [
	path('',views.post_list,name='post_list'),
	path('Profile/new', views.profile_new, name='profile_new'),
	path('register/', views.register, name='register'),
	path('main/', views.main, name='main'),
	path('login/', views.signUp, name='login'),
	path('logout/', views.signOut, name='logout'),
	path('forget/', views.forget, name='forget'),
]