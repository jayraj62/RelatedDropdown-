from django.db import models

# Create your models here.

class Userinfo(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    hobbies=models.CharField(max_length=100)
    countriesid=models.IntegerField()
    statesid=models.IntegerField()
    citiesid=models.IntegerField()


class Country(models.Model):
    id=models.IntegerField(primary_key=True)
    country_name=models.CharField(max_length=30)

class State(models.Model):
    id=models.IntegerField(primary_key=True)
    state_name=models.CharField(max_length=25)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)

class City(models.Model):
    id=models.IntegerField(primary_key=True)
    city_name=models.CharField(max_length=25)
    state=models.ForeignKey(State,on_delete=models.CASCADE)

