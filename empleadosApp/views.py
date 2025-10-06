from django.shortcuts import render
from empleadosApp.models import Empleado
from empleadosApp.forms import EmpleadoRegistroForm
# importar para hacer redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

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
            form.save()
            form = EmpleadoRegistroForm()
            return HttpResponseRedirect(reverse('empleadosData'))

    data = {'form' : form}
    return render(request, 'empleadosApp/empleadoRegistro.html', data)
