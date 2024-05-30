from rest_framework import serializers
from .models import Ingrediensts,Recipes

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediensts
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = '__all__'
