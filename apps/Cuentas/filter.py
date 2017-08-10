import django_filters
from apps.Cuentas.models import Tipos_Documentos

class TiposDocumentos_Filter(django_filters.FilterSet):
    class meta:
        model = Tipos_Documentos
        fields = ['Estado', 'Cuenta_Contable']