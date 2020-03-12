from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from medicar.models import Medico, Agenda, Especialidade, Consulta
from rest_framework import filters
from .serializers import EspecialidadeSerializer ,MedicoSerializer, AgendaSerializer, ConsultaSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

from .filters import MedicoFilter

class EspecialidadeViewSet(ReadOnlyModelViewSet):
        queryset = Especialidade.objects.all()
        serializer_class = EspecialidadeSerializer
        filter_backends = [filters.SearchFilter]
        search_fields = ['nome']
        permission_classes = [permissions.IsAuthenticated]

class MedicoViewSet(ReadOnlyModelViewSet):
        queryset = Medico.objects.all()
        serializer_class = MedicoSerializer
        filter_class = MedicoFilter
        filterset_fields = ['nome', 'especialidade']
        permission_classes = [permissions.IsAuthenticated]

class AgendaViewSet(ReadOnlyModelViewSet):
        queryset = Agenda.objects.all()
        serializer_class = AgendaSerializer
        permission_classes = [permissions.IsAuthenticated]


class ConsultaViewSet(ModelViewSet):
        queryset = Consulta.objects.all()
        serializer_class = ConsultaSerializer
        permission_classes = [permissions.IsAuthenticated]