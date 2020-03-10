from rest_framework import routers
from .api.viewsets import EspecialidadeViewSet, MedicoViewSet, AgendaViewSet, HorarioViewSet

router = routers.DefaultRouter()
router.register(r'especialidade', EspecialidadeViewSet, basename='Especialidade')
router.register(r'medico', MedicoViewSet, basename='Medico')
router.register(r'agenda', AgendaViewSet, basename='Agenda')
router.register(r'horario', HorarioViewSet, basename='Horario')