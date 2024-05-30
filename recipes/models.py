from django.db import models

# Create your models here.
class Ingrediensts(models.Model):
    name = models.CharField(max_length=50)

class Recipes(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    ingredients = models.ForeignKey(Ingrediensts,on_delete= models.CASCADE)

