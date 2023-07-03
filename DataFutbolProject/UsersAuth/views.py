from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from .models import Equipos, Jugadores
from .forms import JugadorForm

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('/')

def profile(request): 
    return render(request, 'profile.html')

def home(request): 
    return render(request, 'home.html')

def equipos(request): 
    equipos = Equipos.objects.all()
    return render(request, 'equipos.html', {'equipos': equipos})

def jugadores(request): 
    equipos = Equipos.objects.all()
    jugadores = Jugadores.objects.all()
    equipo_id = request.GET.get('equipo_id')

    if equipo_id:
        jugadores = jugadores.filter(equipo_id=equipo_id)
    else:
        jugadores = [] 
    return render(request, 'jugadores.html', {'equipos': equipos, 'jugadores': jugadores})

def registrarJugador(request):
    nombre=request.POST['nombre']
    posicion=request.POST['posicion']
    nacimiento=request.POST['nacimiento']
    altura=request.POST['altura']
    nacionalidad=request.POST['nacionalidad']
    equipo=request.POST['equipo_id_create']

    jugador=Jugadores.objects.create(nombre=nombre, posicion=posicion, nacimiento=nacimiento, altura=altura, nacionalidad=nacionalidad, equipo_id=equipo)
    return render(request, 'home.html')

def eliminarJugador(request,jugador_id):
    jugador=Jugadores.objects.get(jugador_id=jugador_id)
    jugador.delete()
    return render(request, 'home.html')

def editarJugador(request, jugador_id):
    jugador=Jugadores.objects.get(jugador_id=jugador_id)
    return render(request, 'editarJugador.html', {'jugador': jugador})

def editarJugadorTemplate(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    posicion=request.POST['posicion']
    nacimiento=request.POST['nacimiento']
    altura=request.POST['altura']
    nacionalidad=request.POST['nacionalidad']

    jugador=Jugadores.objects.get(jugador_id=id)
    jugador.nombre = nombre
    jugador.posicion = posicion
    jugador.nacimiento = nacimiento
    jugador.altura = altura
    jugador.nacionalidad = nacionalidad
    jugador.save()

    return render(request, 'home.html')

def competiciones(request): 
    return render(request, 'competiciones.html')
