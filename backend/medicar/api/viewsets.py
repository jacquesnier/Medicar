from rest_framework.viewsets import ModelViewSet
from medicar.models import Medico, Agenda, Especialidade,Horario
from rest_framework import filters
from .serializers import EspecialidadeSerializer ,MedicoSerializer, AgendaSerializer, HorarioSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import MultipleChoiceFilter, ModelChoiceFilter

class HorarioViewSet(ModelViewSet):
        queryset = Horario.objects.all()
        serializer_class = HorarioSerializer
        permission_classes = [permissions.IsAuthenticated]

class EspecialidadeViewSet(ModelViewSet):
        queryset = Especialidade.objects.all()
        serializer_class = EspecialidadeSerializer
        filter_backends = [filters.SearchFilter]
        search_fields = ['nome']
        permission_classes = [permissions.IsAuthenticated]

class MedicoViewSet(ModelViewSet):
        queryset = Medico.objects.all()
        serializer_class = MedicoSerializer
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['nome', 'especialidade']
        permission_classes = [permissions.IsAuthenticated]

class AgendaViewSet(ModelViewSet):
        queryset = Agenda.objects.all()
        serializer_class = AgendaSerializer
        permission_classes = [permissions.IsAuthenticated]