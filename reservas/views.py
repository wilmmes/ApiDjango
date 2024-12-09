from rest_framework import viewsets
from .models import Cliente, Profesional, Cita, HistorialAtencion
from .serializers import ClienteSerializer, ProfesionalSerializer, CitaSerializer, HistorialAtencionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Vistas para los ModelViewSets
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProfesionalViewSet(viewsets.ModelViewSet):
    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

# Vista Custom para Historial de atención
@api_view(['GET'])
def historial_atencion(request, cita_id):
    try:
        cita = Cita.objects.get(id=cita_id)
        historial = HistorialAtencion.objects.filter(cita=cita)
        serializer = HistorialAtencionSerializer(historial, many=True)
        return Response(serializer.data)
    except Cita.DoesNotExist:
        return Response({"error": "Cita no encontrada"}, status=404)
