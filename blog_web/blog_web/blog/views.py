from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Articulo, Avatar
from .forms import CrearUsuarioForm, ArticuloSearchForm, CrearArticuloForm, CrearAvatarForm, EditarUsuarioForm, CrearComentarioForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# Create your views here.

def view_buscar_articulo_form(request):
    if request.method == "GET":
        form = ArticuloSearchForm()
        return render(
            request, "blog_web/buscar-articulo.html", context={"search_form": form}
        )
    elif request.method == "POST":
        #  devolverle al "explorador" la lista de articulos encontrada o avisa que no se encontró nada
        form = ArticuloSearchForm(request.POST)
        if form.is_valid():
            titulo_art = form.cleaned_data["titulo"]#[]se usa el campo puesto en el formulario
            lista_articulos = Articulo.objects.filter(
            Q(titulo__icontains = titulo_art)
        ).distinct()
        contexto_dict = {"arts": lista_articulos}
        return render(request, "blog_web/lista_articulos.html", contexto_dict)
    
def view_todos_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'blog_web/lista_articulos.html', {'arts':articulos})

def view_crear_articulo(request):
    if request.method == "GET":
        contexto = {"form": CrearArticuloForm()}
        return render(request, "blog_web/crear-articulo.html", contexto)
    elif request.method == "POST":
            form = CrearArticuloForm(request.POST)
            if form.is_valid():
             titulo = form.cleaned_data["titulo"]
             contenido = form.cleaned_data["contenido"]
             imagen = form.cleaned_data["imagen"]
             autor = form.cleaned_data["autor"]
             nuevo_articulo = Articulo(
                titulo=titulo,
                contenido=contenido,
                imagen=imagen,
                autor=autor,
            )
            nuevo_articulo.save()
            return view_articulo_detalles(request, nuevo_articulo.id_articulo)

#def view_articulo_detalles(request, art_id):
#    articulo = Articulo.objects.get(id_articulo=art_id)
#   
#    return render(request, 'blog_web/detalles_articulo.html', {'art':articulo}) #'comentarios':comentarios, 'formulario':form})

def view_crear_usuario_form(request):
    data = {
        'form': CrearUsuarioForm()
    }

    if request.method == 'POST':
        formulario=CrearUsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save() #guarda el formulario si los datos que vinieron son validos
            data["mensaje"] = "Usuario Creado"
            return redirect('home')
        else:
            data["form"] = formulario #si el formulario tiene datos invaliods reenvio el formulario
    return render(request, 'blog_web/crear-usuario.html', data)

def view_iniciar_sesion(request):
    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.user_cache
            if user is not None:
                login(request, user)
                return redirect("home")

    return render(request, "blog_web/iniciar_sesion.html", {"usr": form})

def view_cerrar_sesion(request):
    logout(request)
    return redirect("iniciar-sesion")

def view_gestionar_articulo(request):
    articulos = Articulo.objects.all()
    return render(request, 'blog_web/gestion_articulos.html', {'arts':articulos})

def view_edicion_articulo(request, id):
    articulo = Articulo.objects.get(id_articulo=id)
    return render(request, 'blog_web/editar_articulo.html', {'art': articulo})

def view_editar_articulo(request, id):
    articulo_a_editar = Articulo.objects.filter(id_articulo=id).first()
    if request.method == "GET":
        valores_iniciales = {
            #"id_articulo": articulo_a_editar.id_articulo,
            "titulo": articulo_a_editar.titulo,
            "contenido": articulo_a_editar.contenido,
            "imagen": articulo_a_editar.imagen,
            "autor": articulo_a_editar.autor,
        }
        formulario = CrearArticuloForm(initial=valores_iniciales)
        contexto = {"form": formulario, "art": articulo_a_editar}
        return render(request, "blog_web/editar_articulo.html", contexto)
    elif request.method == "POST":
        form = CrearArticuloForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data["titulo"]
            contenido = form.cleaned_data["contenido"]
            imagen = form.cleaned_data["imagen"]
            autor = form.cleaned_data["autor"]
            articulo_a_editar.titulo = titulo
            articulo_a_editar.contenido = contenido
            articulo_a_editar.imagen = imagen
            articulo_a_editar.autor = autor
            articulo_a_editar.save()
            return redirect("detalles-articulo", articulo_a_editar.id_articulo)
        
def view_borrar_articulo(request, id):
    articulo_a_borrar = Articulo.objects.filter(id_articulo=id).first()
    articulo_a_borrar.delete()
    return redirect("gestion-articulos")

def view_about(request):
    return render(request,"blog_web/about.html")

def view_avatar(request):
    if request.method == "GET":
        contexto = {"AVATAR": CrearAvatarForm()}
    else:
        form = CrearAvatarForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]
            avatar_existente = Avatar.objects.filter(user=request.user)
            avatar_existente.delete()
            nuevo_avatar = Avatar(image=image, user=request.user)
            nuevo_avatar.save()
            return redirect("home")
        else:
            contexto = {"AVATAR": form}

    return render(request, "blog_web/agregar_avatar.html", context=contexto)


class EditarUsuarioView(LoginRequiredMixin, UpdateView):
    
    model = User
    form_class = EditarUsuarioForm
    template_name = 'blog_web/editar_usuario.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

def view_articulo_detalles(request, art_id):
    articulo = Articulo.objects.get(id_articulo=art_id)
    comentarios = articulo.comentarios.filter(activo=True)
    if request.method == 'POST':
        form = CrearComentarioForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False) #esto hace que no se guarde hasta que el Usuario haga click en el boton
            new_form.articulo = articulo
            new_form.save()
    else:
        form = CrearComentarioForm
    return render(request, 'blog_web/detalles_articulo.html', {'art':articulo, 'comentarios':comentarios, 'formulario':form})