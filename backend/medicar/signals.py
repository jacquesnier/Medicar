from django.db.models import signals
from django.dispatch import receiver
from medicar import models

@receiver(signals.post_save, sender=models.Consulta)
def update_agenda_when_save_consulta(sender, instance, **kwargs):
    consulta = instance
    consulta.agenda.disponivel = False
    consulta.agenda.save()

@receiver(signals.post_delete, sender=models.Consulta)
def update_agenda_when_delete_consulta(sender, instance, **kwargs):
    consulta = instance
    consulta.agenda.disponivel = True
    consulta.agenda.save()