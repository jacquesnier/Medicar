from django.db import models
from rest_framework import serializers

class Horario(models.Model):
    horarios = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.horarios

class Especialidade(models.Model):
    nome = models.CharField(max_length=150, blank=False)
    
    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=120, blank=False)
    CRM = models.CharField(max_length=10, blank=False)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=13)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

    def __str__(self):  
        return "Medico: " + self.nome + ", CRM: " + self.CRM + ", Especialidade: " + str(self.especialidade) + ", Telefone: " + self.telefone

class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data = models.DateField()
    disponibilidade = models.ForeignKey(Horario, on_delete=models.CASCADE)
    

    def __str__(self):
        return "Medico: " + str(self.medico.nome) + ", Especialidade: " + str(self.medico.especialidade) + ", Data: " + str(self.data) + ", Disponibilidade: " + str(self.disponibilidade)