from django.shortcuts import render
from empleadosApp.models import Empleado

# Create your views here.
def empleadosData(request):
    empleados = Empleado.objects.all()
    data = {'empleados' : empleados }
    return render(request, 'empleadosApp/empleados.html', data)