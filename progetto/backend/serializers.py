from rest_framework import serializers
from .models import Viaggi

class ViaggiSerializers(serializers.ModelSerializer):
    class Meta:
        model = Viaggi
        fields = "__all__"