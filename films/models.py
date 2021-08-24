from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Film(models.Model):
    title = models.CharField(max_length=80)
    release_date = models.DateTimeField(auto_now_add=False,default=datetime.date.today)
    created_in_countries = models.ForeignKey(Country,related_name='created_in', on_delete=models.PROTECT)
    available_in_countries = models.ManyToManyField(Country, blank=True,related_name='available_in')
    category = models.ManyToManyField(Category, blank=True)
    director = models.ManyToManyField(Director, blank=True)
    def __str__(self):
        return self.title

class Poster(models.Model):
    image = models.ImageField()
    explanation_img = models.CharField(max_length=80)
    film = models.OneToOneField(Film,on_delete=models.CASCADE)

class Commentary(models.Model):
        stars = models.CharField(max_length=1)
        comment = models.CharField(max_length=500)
        film = models.ForeignKey(Film, on_delete=models.CASCADE)
        author = models.ForeignKey(User,on_delete=models.CASCADE)




