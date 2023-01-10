from django import forms
from .models import Familia
from .models import Miembro
from .models import IngresoGasto
from .models import Ubicacion

class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = ['nombre', 'miembros']
        
class MiembroForm(forms.ModelForm):
    class Meta:
        model = Miembro
        fields = ['nombre', 'edad', 'genero']

class IngresoGastoForm(forms.ModelForm):
    class Meta:
        model = IngresoGasto
        fields = ['fuente_ingreso', 'cantidad_ingresos', 'tipo_gasto', 'cantidad_gastos']

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['ciudad', 'pais', 'direccion']     
        
class BusquedaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    edad_desde = forms.IntegerField()
    edad_hasta = forms.IntegerField()
    genero = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Femenino')])           
