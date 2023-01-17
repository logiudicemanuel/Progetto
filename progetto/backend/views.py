from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .serializers import ViaggiSerializers
from .models import Viaggi

# Create your views here.

class ViaggiViewSet(viewsets.ModelViewSet):
    queryset = Viaggi.objects.all()
    serializer_class = ViaggiSerializers