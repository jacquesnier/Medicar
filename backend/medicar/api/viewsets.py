from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from medicar.models import Medico, Agenda, Especialidade, Consulta
from rest_framework import filters
from .serializers import EspecialidadeSerializer ,MedicoSerializer, AgendaSerializer, ConsultaSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
import datetime

from .filters import MedicoFilter, AgendaFilter

class EspecialidadeViewSet(ReadOnlyModelViewSet):
        """
        get: É necessário usuário estar logado.
        list: Retorna uma lista com todas as especialidades cadastradas.
        read: Necessário informar o id da especialidade como parâmetro na url, e retorna as informações detalhadas da especialidade
        """
        queryset = Especialidade.objects.all()
        serializer_class = EspecialidadeSerializer
        filter_backends = [filters.SearchFilter]
        search_fields = ['nome']
        permission_classes = [permissions.IsAuthenticated]

class MedicoViewSet(ReadOnlyModelViewSet):
        """
        list: Retorna uma lista com todos o médicos cadastrados.
        read: Necessário informar o id do médico como parâmetro na url, e retorna as informações detalhadas do médico
        post:

        """

        queryset = Medico.objects.all()
        serializer_class = MedicoSerializer
        filter_class = MedicoFilter
        filterset_fields = ['nome', 'especialidade']
        permission_classes = [permissions.IsAuthenticated]

class AgendaViewSet(ReadOnlyModelViewSet):
        """
        get:
        list: Retorna uma lista com todas as agendas disponíveis.
        read: Necessário informar o id da agenda como parâmetro na url, e retorna as informações detalhadas da agenda
        """
        queryset = Agenda.objects.all()
        serializer_class = AgendaSerializer
        filter_class = AgendaFilter
        filterset_fields = ['medico']
        permission_classes = [permissions.IsAuthenticated]

        def get_queryset(self):
                data_atual = datetime.date.today()
                return Agenda.objects.all().filter(disponivel = True,  dia__gte=data_atual).order_by('dia', 'horario')

        
class ConsultaViewSet(ModelViewSet):
        """
        list: Retorna uma lista com todas as consultas marcadas para o usuário logado. Não exibe consultas passadas
        read: Necessário informar o id da consulta como parâmetro na url, e retorna as informações da consulta
        create: Cria uma nova consulta para o usuário logado. Retorna a consulta marcada 
        update: Atualiza uma consulta já marcada para o usuário logado. Necessário informar o id da consulta como parâmetro na url. Retorna a consulta atualizada
        partial_update: Atualiza uma consulta já marcada para o usuário logado. Necessário informar o id da consulta como parâmetro na url. Retorna a consulta atualizada
        delete: Deleta uma consulta para o usuário logado. Necessário informar o id da consulta como parâmetro na url. Retorna a lista de consultas marcadas para usuário logado
        """
        serializer_class = ConsultaSerializer
        permission_classes = [permissions.IsAuthenticated]

        def get_queryset(self):
                paciente = self.request.user
                data_atual = datetime.date.today()
                queryset = Consulta.objects.all().filter(paciente=paciente, agenda__dia__gt=data_atual).order_by('agenda__dia', 'agenda__horario')

                return queryset