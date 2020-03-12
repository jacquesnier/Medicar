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

class ConsultaSerializer(serializers.ModelSerializer):
    paciente = serializers.StringRelatedField()
    dia = serializers.StringRelatedField(read_only=True, source='agenda.dia')
    horario = serializers.StringRelatedField(read_only=True, source='agenda.horario')

    class Meta:
        model = Consulta
        fields = ('id', 'paciente', 'agenda', 'dia', 'horario', 'data_agendamento')