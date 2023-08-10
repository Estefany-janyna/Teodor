from django.shortcuts import render
from .forms import CalculationForm

def formulario(request):
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            num1 = data['num1']
            num2 = data['num2']
            operation = data['operation']
            if operation == 'add':
                respuesta = num1 + num2
            elif operation == 'sub':
                respuesta = num1 - num2
            else:
                respuesta = num1 * num2
            return render(request, 'formulario1/respuesta.html', {'respuesta': respuesta})
    else:
        form = CalculationForm()
    return render(request, 'formulario1/formulario.html', {'form': form})