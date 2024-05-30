from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipes
from .constants import Rateing_Choice
# Create your models here.

class Rating (models.Model):
    rating = models.CharField(max_length=10,choices=Rateing_Choice)
    recipe = models.ForeignKey(Recipes,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comments(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    recipe= models.ForeignKey(Recipes,on_delete=models.CASCADE)
    content = models.TextField()