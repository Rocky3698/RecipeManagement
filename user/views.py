from django.shortcuts import render
from rest_framework import viewsets
from .models import Comments, Rating
from .serializers import CommentSerializer,RatingSerializer
# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer