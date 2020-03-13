from django.db.models import signals
from django.dispatch import receiver
from medicar import models

@receiver(signals.pre_save, sender=models.Consulta)
def update_agenda_when_save_consulta(sender, instance, **kwargs):

    consulta = instance
    consulta.agenda.disponivel = False


@receiver(signals.pre_delete, sender=models.Consulta)
def update_agenda_when_delete_consulta(sender, instance, **kwargs):

    consulta = instance
    consulta.agenda.disponivel = True      