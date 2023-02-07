from rest_framework import viewsets, filters
from .serializers import ViaggiFattiSerializers
from .serializers import ViaggiDaFareSerializers
from .models import ViaggiFatti
from .models import ViaggiDaFare

# Create your views here.

#VIAGGI FATTI
class ViaggiFattiViewSet(viewsets.ModelViewSet):

    def get_queryset(self): #permette la visualizzazione dei dati limitata all'utente attualmente loggato
        user = self.request.user
        if not user.is_anonymous : 
            return ViaggiFatti.objects.filter(Autore=user)
        return ViaggiFatti.objects.none()

    serializer_class = ViaggiFattiSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Titolo','Data','Luogo',)

    def perform_create(self, serializer):#assegna automaticamente l'utente loggato come autore
        serializer.save(Autore=self.request.user)

class RicercaTitoloVF(viewsets.ModelViewSet):#ricerca solo per titolo

    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous : 
            return ViaggiFatti.objects.filter(Autore=user)
        return ViaggiFatti.objects.none()
        
    serializer_class = ViaggiFattiSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Titolo',)

class RicercaDataVF(viewsets.ModelViewSet):#ricerca solo per data

    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous : 
            return ViaggiFatti.objects.filter(Autore=user)
        return ViaggiFatti.objects.none()

    serializer_class = ViaggiFattiSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Data',)

class RicercaLuogoVF(viewsets.ModelViewSet):#ricerca solo per luogo

    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous : 
            return ViaggiFatti.objects.filter(Autore=user)
        return ViaggiFatti.objects.none()

    serializer_class = ViaggiFattiSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Luogo',)

#VIAGGI DA FARE
class ViaggiDaFareViewSet(viewsets.ModelViewSet):

    def get_queryset(self):#permette la visualizzazione dei dati limitata all'utente attualmente loggato
        user = self.request.user
        if not user.is_anonymous : 
            return ViaggiDaFare.objects.filter(Autore=user)
        return ViaggiDaFare.objects.none()
    
    serializer_class = ViaggiDaFareSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Titolo','Data','Luogo',)

    def perform_create(self, serializer):#assegna automaticamente l'utente loggato come autore
        serializer.save(Autore=self.request.user)

class RicercaTitoloVdF(viewsets.ModelViewSet):#ricerca solo per titolo

    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous : 
            return ViaggiDaFare.objects.filter(Autore=user)
        return ViaggiDaFare.objects.none()

    serializer_class = ViaggiDaFareSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Titolo',)

class RicercaDataVdF(viewsets.ModelViewSet):#ricerca solo per data

    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous : 
            return ViaggiDaFare.objects.filter(Autore=user)
        return ViaggiDaFare.objects.none()

    serializer_class = ViaggiDaFareSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Data',)

class RicercaLuogoVdF(viewsets.ModelViewSet):#ricerca solo per luogo

    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous : 
            return ViaggiDaFare.objects.filter(Autore=user)
        return ViaggiDaFare.objects.none()

    serializer_class = ViaggiDaFareSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Luogo',)
    
