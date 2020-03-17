from rest_framework import serializers
from medicar.models import Medico, Agenda, Especialidade, Consulta
import datetime

class EspecialidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Especialidade
        fields = ('__all__')

class MedicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medico
        fields = ('__all__')
        depth = 1

class AgendaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Agenda
        fields = ('__all__')
        depth = 2

class ConsultaSerializer(serializers.ModelSerializer):
    paciente = serializers.HiddenField(
    default=serializers.CurrentUserDefault())
    dia = serializers.StringRelatedField(read_only=True, source='agenda.dia')
    horario = serializers.StringRelatedField(read_only=True, source='agenda.horario')
    medico = MedicoSerializer(read_only=True, source='agenda.medico')
    
    def validate(self, data):
        data_atual = datetime.date.today()
        hora_atual = datetime.datetime.now().time()
        agenda_selecionada = data['agenda']

        consulta_paciente = Consulta.objects.all().filter(paciente=data['paciente'])

        if agenda_selecionada.dia < data_atual:
            raise serializers.DjangoValidationError('Não foi possível marcar consulta: Dia passado!')
        if (agenda_selecionada.dia == data_atual) and (agenda_selecionada.horario < hora_atual):
            raise serializers.DjangoValidationError('Não foi possível marcar consulta: Horário passado!')
        if consulta_paciente.filter(agenda__dia=agenda_selecionada.dia, agenda__horario=agenda_selecionada.horario):
            raise serializers.DjangoValidationError('Não foi possível marcar consulta: Há uma outra consulta marcada para mesmo dia e horário!')
    
        return data

    class Meta:
        model = Consulta
        fields = ('id', 'dia', 'horario', 'data_agendamento', 'medico', 'paciente', 'agenda')