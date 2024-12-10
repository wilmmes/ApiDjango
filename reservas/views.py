from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cliente, Profesional, Cita
from .serializers import ClienteSerializer, ProfesionalSerializer, CitaSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ProfesionalViewSet(ModelViewSet):
    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer


class CitaViewSet(ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer


@api_view(['GET'])
def custom_api(request):
    return Response({"mensaje": "API personalizada funcionando correctamente"})
