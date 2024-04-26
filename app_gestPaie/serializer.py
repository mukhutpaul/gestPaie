from rest_framework import serializers
from app_gestPaie.models.frais import Frais

class FraisSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Frais
        fields = "__all__"
