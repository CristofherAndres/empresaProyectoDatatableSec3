from django.shortcuts import render
from empleadosApp.models import Empleado
from empleadosApp.forms import EmpleadoRegistroForm

# Create your views here.
def empleadosData(request):
    empleados = Empleado.objects.all()
    data = {'empleados' : empleados }
    return render(request, 'empleadosApp/empleados.html', data)

def crearEmpleado(request):
    form = EmpleadoRegistroForm()

    if request.method == 'POST':
        form = EmpleadoRegistroForm(request.POST)
        if form.is_valid():
            print("Formulario valido")
            print("Nombre: ", form.cleaned_data['nombre'])
            print("Email: ", form.cleaned_data['email'])
            print("Telefono: ", form.cleaned_data['telefono'])

    data = {'form' : form}
    return render(request, 'empleadosApp/empleadoRegistro.html', data)
