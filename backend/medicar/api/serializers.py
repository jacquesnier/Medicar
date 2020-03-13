from rest_framework import serializers
from medicar.models import Medico, Agenda, Especialidade, Consulta

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
    
    class Meta:
        model = Consulta
        fields = ('id', 'dia', 'horario', 'data_agendamento', 'medico', 'paciente', 'agenda')