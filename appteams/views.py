from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
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
def ver_jugadores(request):
    ver_jugadores = models.jugadores.objects.all()  
    return render(request,'jugadores.html',{
        'jugadores' : ver_jugadores
    })

def ver_coachs(request):
    ver_coachs = models.coachs.objects.all()  
    return render(request,'coachs.html',{
        'coachs' : ver_coachs
    })

def ver_ligas(request):
    ver_ligas = models.League.objects.all()
    return render(request, 'ligas.html', {
        'ligas': ver_ligas
    })

def ver_juegos(request):
    ver_juegos = models.Play.objects.all()
    return render(request, 'plays.html', {
        'juegos': ver_juegos
    })

def ver_estadios(request):
    ver_estadios = models.estadios.objects.all()
    return render(request, 'estadios.html', {
        'estadios': ver_estadios
    })

def ver_arbitros(request):
    ver_arbitros = models.arbitros.objects.all()
    return render(request, 'arbitros.html', {
        'arbitros': ver_arbitros
    })
#Funciones de eliminar

def eliminarJugador(request,id):
    jugador = models.jugadores.objects.get(id = id)
    jugador.delete()
    return redirect('http://127.0.0.1:8000/jugadores/')

def eliminarCoach(request,id):
    coach = models.coachs.objects.get(id = id)
    coach.delete()
    return redirect('http://127.0.0.1:8000/coachs/')

def eliminarEquipos(request,id):
    equipo = models.equipos.objects.get(id = id)
    equipo.delete()
    return redirect('http://127.0.0.1:8000/equipos/')

def eliminarArbitros(request,id):
    arbitro = models.arbitros.objects.get(id = id)
    arbitro.delete()
    return redirect('http://127.0.0.1:8000/arbitros/')

def eliminarLigas(request,id):
    liga = models.ligas.objects.get(id = id)
    liga.delete()
    return redirect('http://127.0.0.1:8000/League/')

def eliminarCedulas(request,id):
    cedula = models.cedulas.objects.get(id = id)
    cedula.delete()
    return redirect('http://127.0.0.1:8000/cedulas/')

def eliminarJuegos(request,id):
    juego = models.plays.objects.get(id = id)
    juego.delete()
    return redirect('http://127.0.0.1:8000/plays/')

def eliminarEstadios(request,id):
    estadio = models.estadios.objects.get(id = id)
    estadio.delete()
    return redirect('http://127.0.0.1:8000/estadios/')

#Funciones de editar

def editarJugador(request,id):
    form = None 
    error = None
    try:
        jugador = models.jugadores.objects.get(id = id)
        if request.method == 'GET':
            form = jugadores(instance = jugador)
        else:
            form = jugadores(request.POST, request.FILES,instance = jugador)
            if form.is_valid():
                form.save()
            return redirect('http://127.0.0.1:8000/jugadores/')
    except ObjectDoesNotExist as e:
        error = e
    
    return render(request,'formulario.html',{'form':form,'error':error})

def editarCedula(request,id):
    form = None 
    error = None
    try:
        cedula = models.cedulas.objects.get(id = id)
        if request.method == 'GET':
            form = cedulas(instance = cedula)
        else:
            form = cedulas(request.POST, request.FILES,instance = cedula)
            if form.is_valid():
                form.save()
            return redirect('http://127.0.0.1:8000/cedulas/')
    except ObjectDoesNotExist as e:
        error = e
    
    return render(request,'formulario.html',{'form':form,'error':error})

def editarEquipo(request,id):
    form = None 
    error = None
    try:
        equipo = models.equipos.objects.get(id = id)
        if request.method == 'GET':
            form = equipos(instance = equipo)
        else:
            form = equipos(request.POST, request.FILES,instance = equipo)
            if form.is_valid():
                form.save()
            return redirect('http://127.0.0.1:8000/equipos/')
    except ObjectDoesNotExist as e:
        error = e
    
    return render(request,'formulario.html',{'form':form,'error':error})

def editarArbitro(request,id):
    form = None 
    error = None
    try:
        arbitro = models.arbitros.objects.get(id = id)
        if request.method == 'GET':
            form = arbitros(instance = arbitro)
        else:
            form = arbitros(request.POST, request.FILES,instance = arbitro)
            if form.is_valid():
                form.save()
            return redirect('http://127.0.0.1:8000/equipos/')
    except ObjectDoesNotExist as e:
        error = e
    
    return render(request,'formulario.html',{'form':form,'error':error})

def editarCoach(request,id):
    form = None 
    error = None
    try:
        coach = models.coachs.objects.get(id = id)
        if request.method == 'GET':
            form = coachs(instance = coach)
        else:
            form = coachs(request.POST, request.FILES,instance = coach)
            if form.is_valid():
                form.save()
            return redirect('http://127.0.0.1:8000/equipos/')
    except ObjectDoesNotExist as e:
        error = e
    
    return render(request,'formulario.html',{'form':form,'error':error})

def editarEstadio(request,id):
    form = None 
    error = None
    try:
        estadio = models.estadios.objects.get(id = id)
        if request.method == 'GET':
            form = estadios(instance = estadio)
        else:
            form = estadios(request.POST, request.FILES,instance = estadio)
            if form.is_valid():
                form.save()
            return redirect('http://127.0.0.1:8000/equipos/')
    except ObjectDoesNotExist as e:
        error = e
    
    return render(request,'formulario.html',{'form':form,'error':error})

def editarLiga(request,id):
    form = None 
    error = None
    try:
        liga = models.League.objects.get(id = id)
        if request.method == 'GET':
            form = League(instance = liga)
        else:
            form = League(request.POST, request.FILES,instance = liga)
            if form.is_valid():
                form.save()
            return redirect('http://127.0.0.1:8000/equipos/')
    except ObjectDoesNotExist as e:
        error = e
    
    return render(request,'formulario.html',{'form':form,'error':error})
    
def editarJuego(request,id):
    form = None 
    error = None
    try:
        juego = models.Play.objects.get(id = id)
        if request.method == 'GET':
            form = Play(instance = juego)
        else:
            form = Play(request.POST, request.FILES,instance = juego)
            if form.is_valid():
                form.save()
            return redirect('http://127.0.0.1:8000/equipos/')
    except ObjectDoesNotExist as e:
        error = e
    
    return render(request,'formulario.html',{'form':form,'error':error})
        
    
    
    