from django.apps import AppConfig


class MedicarConfig(AppConfig):
    name = 'medicar'

    def ready(self):
        from . import signals
