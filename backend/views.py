from rest_framework import viewsets, filters
from .serializers import ViaggiFattiSerializers
from .serializers import ViaggiDaFareSerializers
from .models import ViaggiFatti
from .models import ViaggiDaFare

# Create your views here.

#VIAGGI FATTI
class ViaggiFattiViewSet(viewsets.ModelViewSet):
    queryset = ViaggiFatti.objects.all()
    serializer_class = ViaggiFattiSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Titolo','Data','Luogo',)

class RicercaTitoloVF(viewsets.ModelViewSet):#FILTRA SOLO PER TITOLO
    queryset = ViaggiFatti.objects.all()
    serializer_class = ViaggiFattiSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Titolo',)

class RicercaDataVF(viewsets.ModelViewSet):#FILTRA SOLO PER DATA
    queryset = ViaggiFatti.objects.all()
    serializer_class = ViaggiFattiSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Data',)

class RicercaLuogoVF(viewsets.ModelViewSet):#FILTRA SOLO PER LUOGO
    queryset = ViaggiFatti.objects.all()
    serializer_class = ViaggiFattiSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Luogo',)

#VIAGGI DA FARE
class ViaggiDaFareViewSet(viewsets.ModelViewSet):
    queryset = ViaggiDaFare.objects.all()
    serializer_class = ViaggiDaFareSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Titolo','Data','Luogo',)

class RicercaTitoloVdF(viewsets.ModelViewSet):#FILTRA SOLO PER TITOLO
    queryset = ViaggiDaFare.objects.all()
    serializer_class = ViaggiDaFareSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Titolo',)

class RicercaDataVdF(viewsets.ModelViewSet):#FILTRA SOLO PER DATA
    queryset = ViaggiDaFare.objects.all()
    serializer_class = ViaggiDaFareSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Data',)

class RicercaLuogoVdF(viewsets.ModelViewSet):#FILTRA SOLO PER LUOGO
    queryset = ViaggiDaFare.objects.all()
    serializer_class = ViaggiDaFareSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Luogo',)
    
