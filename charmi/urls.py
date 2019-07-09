from django.urls import path
from . import views

urlpatterns = [
	path('',views.post_list,name='inicio'),
	path('register/', views.register, name='register'),
	path('main/', views.main, name='main'),
	path('login/', views.signUp, name='login'),
	path('logout/', views.signOut, name='logout'),
	path('forget/', views.forget, name='forget'),
]