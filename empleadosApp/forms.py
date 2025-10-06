from django import forms
from empleadosApp.models import Empleado
from django.core import validators

#Es el formulario para editar
class EmpleadoRegistroForm(forms.Form):
    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(5),
        validators.MaxLengthValidator(10),
    ])
    email = forms.CharField()
    telefono = forms.CharField(required=False)

    def clean_email(self):
        inputEmail = self.cleaned_data['email']
        if inputEmail.find('@') ==-1:
            raise forms.ValidationError("El correo debe contener un @")
        return inputEmail
    
    nombre.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'

#Este es el formulario insertar
class EmpleadoRegistroForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(5),
        validators.MaxLengthValidator(10),
    ])
    email = forms.CharField()
    telefono = forms.CharField(required=False)

    def clean_email(self):
        inputEmail = self.cleaned_data['email']
        if inputEmail.find('@') ==-1:
            raise forms.ValidationError("El correo debe contener un @")
        return inputEmail

    nombre.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'