from django.urls import path
from . import views

urlpatterns = [
	path('',views.post_list,name='inicio'),
	path('register/', views.register, name='register'),
	path('main/', views.main, name='main'),
	path('login/', views.signUp, name='login'),
	path('logout/', views.signOut, name='logout'),
	path('forget/', views.forget, name='forget'),
	path('edit/', views.edit_perfil, name='edit'),
	path('ajedrez/', views.jugar_ajedrez, name='ajedrez'),
	path('rankings/', views.victoria, name='Victoria'),
	path('rankingsd/', views.derrota, name='Derrota'),
	path('rankingse/', views.empate, name='Empate'),
]