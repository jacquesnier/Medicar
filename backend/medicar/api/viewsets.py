from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from medicar.models import Medico, Agenda, Especialidade, Consulta
from rest_framework import filters
from .serializers import EspecialidadeSerializer ,MedicoSerializer, AgendaSerializer, ConsultaSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
import datetime

from .filters import MedicoFilter, AgendaFilter

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
        filter_class = AgendaFilter
        filterset_fields = ['medico']
        permission_classes = [permissions.IsAuthenticated]

        def get_queryset(self):
                data_atual = datetime.date.today()
                return Agenda.objects.all().filter(disponivel = True,  dia__gte=data_atual).order_by('dia', 'horario')

        
class ConsultaViewSet(ModelViewSet):
        serializer_class = ConsultaSerializer
        permission_classes = [permissions.IsAuthenticated]

        def get_queryset(self):
                paciente = self.request.user
                data_atual = datetime.date.today()
                queryset = Consulta.objects.all().filter(paciente=paciente, agenda__dia__gt=data_atual).order_by('agenda__dia', 'agenda__horario')

                return queryset