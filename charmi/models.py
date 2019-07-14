from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Photo(models.Model):
	ruta = models.ImageField(
		upload_to ='../imagenes/Profiles/', height_field=None,
		width_field=None, max_length=100)

class Profile(models.Model):
	Gender = (
		('F','Femenino'),
		('M','Masculo'),
	)

	Sexo = models.CharField(max_length=1, choices = Gender)

	User = models.OneToOneField('auth.User', on_delete=models.CASCADE)
	Photo =models.OneToOneField(Photo, null=True, blank=True, on_delete=models.CASCADE)
	Partidas = models.ForeignKey("Game", null=True, blank=True, on_delete=models.CASCADE)

class Address(models.Model):
	Street = models.CharField(max_length=30, null=True, blank=True, default=None)
	Avenue = models.CharField(max_length=30, null=True, blank=True, default=None)
	City = models.CharField(max_length=30, null=True, blank=True, default=None)
	Country = models.CharField(max_length=30, null=True, blank=True, default=None)

	Profile = models.ForeignKey(Profile, related_name="Addresses", on_delete=models.CASCADE)

class Ranking(models.Model):
	IdRanking = models.AutoField(max_length=30, primary_key=True)
	Type = models.CharField(max_length=30)
	Cantidad = models.IntegerField()
	Num_win = models.IntegerField()
	Num_lose = models.IntegerField()
	Num_draw = models.IntegerField()

	Game = models.ForeignKey("Game_list",related_name="elo", null=True, blank=True, on_delete=models.CASCADE)
	Profile = models.ForeignKey(Profile, related_name="Rankings", null=True, blank=True, on_delete=models.CASCADE)

class Followers(models.Model):
	
	Accept = models.BooleanField(default=False)

	Followers = models.ForeignKey(Profile, null=True,related_name="Followe_profile", blank=True, on_delete=models.CASCADE)
	Follow = models.ForeignKey(Profile, null=True,related_name="Follow_profile", blank=True, on_delete=models.CASCADE)

	class Meta:
		unique_together = ['Followers','Follow']

class Game_list(models.Model):
	IdGame = models.CharField(max_length=30, primary_key=True)
	NameGame = models.CharField(max_length=30)

class Game(models.Model):
	IdPlayGame = models.CharField(max_length=30, primary_key=True)
	Fecha_Hora =  models.DateTimeField()
	Result = models.CharField(max_length=30)

	IdGame = models.ForeignKey(Game_list, related_name="Id_Game",null=True, blank=True, on_delete=models.CASCADE)
