from django import forms
from empleadosApp.models import Empleado

#Es el formulario para editar
class EmpleadoRegistroForm(forms.Form):
    nombre = forms.CharField()
    email = forms.CharField()
    telefono = forms.CharField()

#Este es el formulario insertar
class EmpleadoRegistroForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

    nombre = forms.CharField()
    email = forms.CharField()
    telefono = forms.CharField()

    nombre.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'