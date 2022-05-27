

from django.http import HttpResponse
from django.shortcuts import render
from AppWb import forms

from AppWb.forms import EquiposFormularios, AsociadosFormularios, CursosFormularios, UserRegisterForm
from AppWb.models import Asociados, Cursos, Equipos
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
 #LOGIN
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def login_request(request):
    if request.method =='POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get('username')

            contraseña=form.cleaned_data.get('password')

            user=authenticate(username=usuario, password=contraseña)

            if user:
                login(request, user)
                return render(request, 'AppWb/inicio.html', {'mensaje':f"Bienvenido a Wolrd e-sports {user}"})
        else:

            return render(request, 'AppWb/inicio.html',{'mensaje':"Error. Datos incorrectos"})
    else:
        form=AuthenticationForm()
    return render(request, 'AppWb/login.html',{'form':form})
        

# Create your views here.
def inicio(request):
    return render(request,'AppWb/inicio.html')
def asociados(request):
    if request.method=='POST':
        miFormulario= AsociadosFormularios(request.POST)
        print(miFormulario)


        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            asociados=Asociados(nombre=informacion['nombre'], redes_sociales=informacion['redes_sociales'])
            asociados.save()

            return render(request,"AppWb/inicio.html")
    else:
        miFormulario= AsociadosFormularios()
    return render(request,'AppWb/asociados.html', {'miFormulario':miFormulario})





def cursos(request):
   
    if request.method=='POST':
        miFormulario= CursosFormularios(request.POST)
        print(miFormulario) 


        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            cursos=Cursos(nombre=informacion['nombre'], jugadorpro=informacion['jugadorpro'], duracion=informacion['duracion'])
            cursos.save()

            return render(request,"AppWb/inicio.html")
    else:
        miFormulario= CursosFormularios()
    return render(request,'AppWb/cursos.html', {'miFormulario':miFormulario})

def equipos(request):
    if request.method=='POST':
        miFormulario= EquiposFormularios(request.POST)
        print(miFormulario)


        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            equipos=Equipos(nombre=informacion['nombre'], seguidores=informacion['seguidores'],)
            equipos.save()

            return render(request,"AppWb/inicio.html")
    else:
        miFormulario= EquiposFormularios()
    return render(request,'AppWb/equipos.html', {'miFormulario':miFormulario})

def busquedaSeguidores(request):
    return render(request, 'AppWb/busquedaSeguidores.html')


def buscar(request):
    if request.GET['seguidores']:
        seguidores=request.GET['seguidores']
        equipos=Equipos.objects.filter(seguidores__icontains=seguidores)
        return render(request, "AppWb/resultadoBusqueda.html",{'equipos':equipos, 'seguidores':seguidores})
   # respuesta =f"Estoy este numero de seguidores :{request.GET['seguidores']}"#
    else:
        respuesta ="No enviaste Datos"
        return HttpResponse(respuesta)

def lecturaCursos(request):
    cursos=Cursos.objects.all()
    contexto1= {'cursos':cursos}
    return render(request, 'AppWb/lecturaCursos.html', contexto1)

def eliminarCurso(request, cursos_nombre):

    cursos=Cursos.objects.get(nombre=cursos_nombre)
    cursos.delete()
    
    cursos= Cursos.objects.all()
    contextin= {'cursos': cursos}
    return render(request, 'AppWb/lecturaCursos.html', contextin)


def editarCurso(request,cursos_nombre):
    cursos=Cursos.objects.get(nombre=cursos_nombre)
    if request.method == 'POST':
        miFormulario = CursosFormularios(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():
            
            informacion=miFormulario.cleaned_data

            cursos.nombre = informacion['nombre']
            cursos.jugadorpro=informacion['jugadorpro']
            cursos.duracion=informacion['duracion']

            cursos.save()
            return render(request, 'AppWb/inicio.html')
    else: 
        miFormulario= CursosFormularios(initial={'nombre':cursos.nombre, 'jugadorpro': cursos.jugadorpro, 'duracion': cursos.duracion})
    return render(request, 'AppWb/editarCurso.html', {'miFormulario':miFormulario, 'cursos_nombre':cursos_nombre})


class CursosList( ListView):
    model = Cursos
    template_name = 'AppWb/curso_list.html'
class CursosDetalle( DetailView):
    model = Cursos
    template_name = 'AppWb/cursos_detalle.html'
class CursosCreacion( CreateView):
    model = Cursos
    success_url = '/AppWb/curso/list'
    fields = ['nombre', 'jugadorpro','duracion']
class CursosUpdate( UpdateView):
    model = Cursos
    success_url = '/AppWb/cursos/list'
    fields = ['nombre', 'jugadorpro','duracion']
class CursosDelete( DeleteView):
    model = Cursos
    success_url = '/AppWb/curso/list'


