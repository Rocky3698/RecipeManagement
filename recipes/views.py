from django.shortcuts import render
from rest_framework import viewsets
from .models import Recipes 
from .serializers import RecipeSerializer
# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer