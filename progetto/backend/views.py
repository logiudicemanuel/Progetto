from rest_framework import viewsets
from .serializers import ViaggiFattiSerializers
from .serializers import ViaggiDaFareSerializers
from .models import ViaggiFatti
from .models import ViaggiDaFare
# Create your views here.

class ViaggiFattiViewSet(viewsets.ModelViewSet):
    queryset = ViaggiFatti.objects.all()
    serializer_class = ViaggiFattiSerializers

class ViaggiDaFareViewSet(viewsets.ModelViewSet):
    queryset = ViaggiDaFare.objects.all()
    serializer_class = ViaggiDaFareSerializers
