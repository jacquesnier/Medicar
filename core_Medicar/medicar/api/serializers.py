from rest_framework.serializers import ModelSerializer
from medicar.models import Medico, Agenda, Especialidade, Horario
from rest_framework.exceptions import ValidationError

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
    class Meta:
        model = Agenda
        fields = ('__all__')
    
    