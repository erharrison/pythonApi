from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ImagePostSerializer
from .models import ImagePost


class ImagePostViewSet(viewsets.ModelViewSet):
    queryset = ImagePost.objects.all().order_by('id')
    serializer_class = ImagePostSerializer
