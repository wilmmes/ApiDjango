from rest_framework import serializers
from .models import Cliente, Profesional, Cita, HistorialAtencion

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional
        fields = '__all__'


class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'


class HistorialAtencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialAtencion
        fields = '__all__'
