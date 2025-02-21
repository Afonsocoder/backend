from rest_framework import viewsets
from .serializers import PacienteSerializer
from app_principal.models import Paciente

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer