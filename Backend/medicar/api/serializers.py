from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from medicar.models import Medico, Agenda, Especialidade, Horario
from rest_framework.exceptions import ValidationError
from datetime import date

class HorarioSerializer(ModelSerializer):

    class Meta:
        model = Horario
        fields = ('__all__')

class EspecialidadeSerializer(ModelSerializer):

    class Meta:
        model = Especialidade
        fields = ('__all__')

class MedicoSerializer(ModelSerializer):

    class Meta:
        model = Medico
        fields = ('__all__')
        depth = 1

class AgendaSerializer(ModelSerializer):
        
    def validate(self, data):
        medico = data['medico']
        dia_marcado = data['dia']
        horario = data['horario']
        data_atual = date.today()

        if data['dia'] < data_atual: 
            raise serializers.ValidationError({
                'Não é permitido criar agendamento para um dia já passado!'
            })

        if Agenda.objects.filter(medico=medico, dia=dia_marcado).exists(): 
            raise serializers.ValidationError({
                'Não é permitido dois agendamentos para o mesmo médico em um mesmo dia!'
            })
        
        return data
    
    class Meta:
        model = Agenda
        fields = ('__all__')
