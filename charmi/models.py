from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Photo(models.Model):
	ruta = models.ImageField(
		upload_to ='imagenes/Profiles/', height_field=None,
		width_field=None, max_length=100)

class Profile(models.Model):
	Gender = (
		('F','Femenino'),
		('M','Masculo'),
	)

	First_name = models.CharField(max_length=30)
	Last_name = models.CharField(max_length=30) 
	Date_Born = models.DateField()
	Date_joined = models.DateField()
	Last_join = models.DateField()

	User = models.OneToOneField(User, on_delete=models.CASCADE)
	Photo =models.OneToOneField(Photo, null=True, blank=True, on_delete=models.CASCADE)
	Jugadores = models.ForeignKey("Game", null=True, blank=True, on_delete=models.CASCADE)

class Address(models.Model):
	Street = models.CharField(max_length=30)
	Avenue = models.CharField(max_length=30)
	City = models.CharField(max_length=30)
	Country = models.CharField(max_length=30)

	Profile = models.ForeignKey(Profile,related_name="Address", null=True, blank=True, on_delete=models.CASCADE)

class Ranking(models.Model):
	IdRanking = models.CharField(max_length=30, primary_key=True)
	Type = models.CharField(max_length=30)
	Num_win = models.CharField(max_length=30)
	Num_lose = models.CharField(max_length=30)
	Num_draw = models.CharField(max_length=30)

	IdGame = models.OneToOneField("Game_list", null=True, blank=True, on_delete=models.CASCADE)
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

class Opponents(models.Model):
	IdOpponents = models.CharField(max_length=30, primary_key=True)
	Opponents = models.CharField(max_length=30)

	Contrincante = models.ForeignKey("Game", null=True, blank=True, on_delete=models.CASCADE)

class Game(models.Model):
	IdPlayGame = models.CharField(max_length=30, primary_key=True)
	Fecha_Hora =  models.DateTimeField()
	Result = models.CharField(max_length=30)

	IdGame = models.OneToOneField(Game_list, null=True, blank=True, on_delete=models.CASCADE)


