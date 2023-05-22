from django.shortcuts import render
from .forms import cedulas,arbitros,equipos,League,Play,jugadores,estadios,coachs
from . import models 

#_________FUNCIONES DE LOS FORMULARIOS____________________
def cedulas_view(request):
    if request.method == 'POST':
        form = cedulas(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            # Realiza alguna acción después de guardar el formulario
    else:
        form = cedulas()

    context = {
        'form': form
    }
    return render(request, 'formulario.html', context)

def arbitros_view(request):
    if request.method == 'POST':
        form = arbitros(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Realiza alguna acción después de guardar el formulario
    else:
        form = arbitros()

    context = {
        'form': form
    }
    return render(request, 'formulario.html', context)

def equipos_view(request):
    if request.method == 'POST':
        form = equipos(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Realiza alguna acción después de guardar el formulario
    else:
        form = equipos()

    context = {
        'form': form
    }
    return render(request, 'formulario.html', context)

def League_view(request):
    if request.method == 'POST':
        form = League(request.POST, request.FILES)
        print("Recibiendo el formulario 2")
        print(form.fields)
        if form.is_valid():
            print("Recibiendo el formulario")
            print(form.fields)
            form.save()
            # Realiza alguna acción después de guardar el formulario
    else:
        form = League()
        print("Entro aqui   ")

    context = {
        'form': form
    }
    return render(request, 'formulario.html', context)

def Play_view(request):
    if request.method == 'POST':
        form = Play(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Realiza alguna acción después de guardar el formulario
    else:
        form = Play()

    context = {
        'form': form
    }
    return render(request, 'formulario.html', context)

def jugadores_view(request):
    if request.method == 'POST':
        form = jugadores(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Realiza alguna acción después de guardar el formulario
    else:
        form = jugadores()

    context = {
        'form': form
    }
    return render(request, 'formulario.html', context)

def estadios_view(request):
    if request.method == 'POST':
        form = estadios(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Realiza alguna acción después de guardar el formulario
    else:
        form = estadios()

    context = {
        'form': form
    }
    return render(request, 'formulario.html', context)

def coachs_view(request):
    if request.method == 'POST':
        form = coachs(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Realiza alguna acción después de guardar el formulario
    else:
        form = coachs()

    context = {
        'form': form
    }
    return render(request, 'formulario.html', context)

##________________FUNCIONES PARA MOSTRAR LA INFO__________________

def ver_equipos(request):
    ver_equipos = models.equipos.objects.all()  
    return render(request,'equipos.html',{
        'equipos' : ver_equipos
    })
    
def ver_cedulas(request):
    ver_cedulas = models.cedulas.objects.all()
    return render(request,'cedulas.html',{
        'cedulas' : ver_cedulas,
    })
