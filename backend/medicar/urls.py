from rest_framework import routers
from .api.viewsets import EspecialidadeViewSet, MedicoViewSet, AgendaViewSet, ConsultaViewSet

router = routers.DefaultRouter()
router.register(r'especialidades', EspecialidadeViewSet, basename='especialidade')
router.register(r'medicos', MedicoViewSet, basename='medico')
router.register(r'agendas', AgendaViewSet, basename='agenda')
router.register(r'consultas', ConsultaViewSet, basename='consulta')

urlpatterns = router.urls