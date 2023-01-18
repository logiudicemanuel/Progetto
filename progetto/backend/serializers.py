from rest_framework import serializers
from .models import ViaggiFatti
from .models import ViaggiDaFare

class ViaggiFattiSerializers(serializers.ModelSerializer):
    class Meta:
        model = ViaggiFatti
        fields = ['Titolo' , 'Data', 'Descrizione', 'Luogo']

class ViaggiDaFareSerializers(serializers.ModelSerializer):
    class Meta:
        model = ViaggiDaFare
        fields = ['Titolo' , 'Data', 'Attivita', 'Luogo']