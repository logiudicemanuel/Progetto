from rest_framework import serializers
from .models import ViaggiFatti
from .models import ViaggiDaFare

class ViaggiFattiSerializers(serializers.ModelSerializer):
    class Meta:
        model = ViaggiFatti
        fields = "__all__"

class ViaggiDaFareSerializers(serializers.ModelSerializer):
    class Meta:
        model = ViaggiDaFare
        fields = "__all__"