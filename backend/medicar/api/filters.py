import django_filters

from medicar.models import Especialidade, Medico

class MedicoFilter(django_filters.FilterSet):
    especialidade = django_filters.filters.ModelMultipleChoiceFilter(
        queryset=Especialidade.objects.all()
    )
    nome = django_filters.filters.CharFilter(
        lookup_expr='icontains'
    )

    class Meta:
        model = Medico
        fields = (
            'nome', 'especialidade'
        )