from django.db import models
from django.contrib.auth.models import User

from rest_framework import serializers


class Especialidade(models.Model):
    nome = models.CharField(max_length=150, blank=False)
    
    def __str__(self):
        return self.nome


class Medico(models.Model):
    nome = models.CharField(max_length=120, blank=False)
    crm = models.CharField(max_length=10, blank=False)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=13)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

    def __str__(self):  
        return "Medico: " + self.nome + ", CRM: " + self.crm + ", Especialidade: " + str(self.especialidade) + ", Telefone: " + self.telefone


class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia = models.DateField()
    horario = models.TimeField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return "Medico: " + str(self.medico.nome) + ", Especialidade: " + str(self.medico.especialidade) + ", Dia: " + str(self.dia) + ", Horario: " + str(self.horario)

    class Meta:
        unique_together = [['medico', 'dia', 'horario']]


class Consulta(models.Model):
    agenda = models.OneToOneField(Agenda, on_delete=models.CASCADE)
    paciente = models.ForeignKey(User, on_delete=models.CASCADE)
    data_agendamento = models.DateTimeField(auto_now=True)