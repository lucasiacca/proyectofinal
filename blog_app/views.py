from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Articulo
from .forms import ImagenFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo 
    fields = ("titulo", "seccion", "subtitulo", "cuerpo", "autor", "imagen")
    success_url = reverse_lazy("lista_articulos")
    

class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo 
    fields = ("titulo", "seccion", "subtitulo", "cuerpo", "autor", "imagen")
    success_url = reverse_lazy("lista_articulos")

class ArticuloDetailView(DetailView): 
    model = Articulo
    success_url = reverse_lazy("lista_articulos")
    
class ArticuloListView(ListView): 
    model = Articulo
    template_name = "blog_app/lista_articulos.html"
    

class ArticuloDeleteView(LoginRequiredMixin, DeleteView): 
    model = Articulo
    success_url = reverse_lazy("lista_articulos")   
    
def buscar_articulo_title(request): 
    if request.method == "POST":
       data = request.POST
       busqueda = data.get("busqueda")
       articulos = Articulo.objects.filter(titulo__contains=busqueda)
       contexto = {"articulos": articulos,}
       
       return render(request, "blog_app/base.html", context = contexto)
    else:
        return render(request, "blog_app/base.html")

def buscar_articulo_autor(request): 
    if request.method == "POST":
       data = request.POST
       busqueda = data.get("busqueda")
       articulos = Articulo.objects.filter(autor__contains=busqueda)
       contexto = {"articulos": articulos,}
       
       return render(request, "blog_app/base.html", context = contexto)
    else:
        return render(request, "blog_app/base.html")   
    
def index(request):
    bienvenida = "Bienvenido al Blog"
    articulos = Articulo.objects.order_by('fecha')
    ultimo_articulo = articulos.latest('fecha')
    anteultimo_articulo = None
    antepenultimo_articulo = None

    if len(articulos) >= 2:
        anteultimo_articulo = articulos[1]

    if len(articulos) >= 3:
        antepenultimo_articulo = articulos[2]

    context = {
        "bienvenida": bienvenida,
        "ultimo_articulo": ultimo_articulo,
        "anteultimo_articulo": anteultimo_articulo,
        "antepenultimoarticulo": antepenultimo_articulo
    }

    if len(articulos) == 0:
        context["mensaje"] = "No existen artículos aún"

    return render(request, "blog_app/inicio.html", context)



def sobre_autor(request): 
    nombre = "Lucas Iaccarino"
    foto = "Blog\Blog\media\Foto_Lucas.jpeg"
    descripcion = "Este es mi primer trabajo practico como programador de Python y Django. \n Me interesa aprender sobre nuevas técnicas y poder implementarlas en mi trabajo"
    context = {"nombre":nombre, "descripcion": descripcion}
    return render(request, "blog_app/inicio.html", context)

def agregar_imagen(request):
  if request.method == "POST":
      formulario = ImagenFormulario(request.POST, request.FILES) 

      if formulario.is_valid():
          avatar = formulario.save()
          avatar.user = request.user
          avatar.save()
          url_exitosa = reverse('inicio')
          return redirect(url_exitosa)
  else:  # GET
      formulario = ImagenFormulario()
  return render(
      request=request,
      template_name="perfiles/formulario_imagen.html",
      context={'form': formulario},
      )


# Create your views here.
