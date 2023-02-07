from rest_framework import serializers
from .models import ViaggiFatti
from .models import ViaggiDaFare
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
class ViaggiFattiSerializers(serializers.ModelSerializer):
    class Meta:
        model = ViaggiFatti
        fields = ["id","Titolo", "Data", "Descrizione", "Luogo"]

class ViaggiDaFareSerializers(serializers.ModelSerializer):

    class Meta:
        model = ViaggiDaFare
        fields = ["id","Titolo", "Data", "Attivita", "Luogo"]