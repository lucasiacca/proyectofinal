from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django import forms
from .models import Articulo
from .forms import ImagenFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo 
    fields = ("titulo", "seccion", "subtitulo", "cuerpo", "imagen_articulo")
    success_url = reverse_lazy("lista_articulos")
    
  
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial['autor'] = self.request.user.username
        return initial

class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo 
    fields = ("titulo", "seccion", "subtitulo", "cuerpo", "autor", "imagen_articulo")
    success_url = reverse_lazy("lista_articulos")

class ArticuloDetailView(DetailView): 
    model = Articulo
    success_url = reverse_lazy("lista_articulos")
    
class ArticuloListView(ListView): 
    model = Articulo
    template_name = "blog_app/lista_articulos.html"
    
class ArticuloSectionListView(ListView): 
    model = Articulo
    template_name = "blog_app/lista_busqueda.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        seccion = self.kwargs.get('seccion')  # Obtener el valor de la sección desde la URL
        if seccion:
            queryset = queryset.filter(seccion=seccion)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seccion = self.kwargs.get('seccion')  # Obtener el valor de la sección desde la URL
        if seccion:
            context['seccion'] = seccion
            if not context['object_list']:
                context['mensaje'] = "No hay artículos en esta sección."
        else:
            context['seccion'] = ""
        return context
    
class ArticuloAutorForm(forms.Form):
    autor = forms.ModelChoiceField(queryset=Articulo.objects.values_list('autor', flat=True).distinct())

class ArticuloAutorListView(ListView):
    model = Articulo
    template_name = "blog_app/lista_busqueda_autor.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        autor = self.request.GET.get('autor')  # Obtener el valor seleccionado del formulario
        if autor:
            queryset = queryset.filter(autor__username=autor)
        return queryset

    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     form = ArticuloAutorForm()
     context['form'] = form
     return context


    



class ArticuloDeleteView(LoginRequiredMixin, DeleteView): 
    model = Articulo
    success_url = reverse_lazy("lista_articulos")   
    
def buscar_articulo_title(request): 
    print("entranda a la prueba")
    if request.method == "POST":
       data = request.POST
       busqueda = data.get("busqueda")
       articulos = Articulo.objects.filter(titulo__contains=busqueda)
       object_list = list(articulos)
       contexto = {"object_list": object_list,}
       
       print(f"Resultados de la búsqueda: {object_list}")
       
       return render(request, "blog_app/lista_busqueda_articulos.html", context = contexto)
    else:
        return render(request, "blog_app/lista_busqueda_articulos.html")

def buscar_articulo_autor(request):
    if request.method == 'POST':
        autor = request.POST.get('busqueda')  # Obtener el nombre del autor desde el formulario
        articulos = Articulo.objects.filter(autor__username__icontains=autor)  # Filtrar artículos por el nombre de usuario del autor
        context = {'articulos': articulos}
        return render(request, 'blog_app/lista_articulos.html', context)
    return render(request, 'blog_app/lista_articulos.html')

  
    
def index(request):
    bienvenida = "Bienvenido al Blog"
    articulos = Articulo.objects.order_by('fecha')
    ultimo_articulo = articulos.latest('fecha')
    anteultimo_articulo = None
    antepenultimo_articulo = None
    mostrar_pagina2 = False
    mostrar_pagina3 = False
    

    if len(articulos) >= 2:
        anteultimo_articulo = articulos[1]

    if len(articulos) >= 3:
        antepenultimo_articulo = articulos[2]
        mostrar_pagina2 = True
    
    if len(articulos) >= 5:
        mostrar_pagina2 = True
        

    context = {
        "bienvenida": bienvenida,
        "ultimo_articulo": ultimo_articulo,
        "anteultimo_articulo": anteultimo_articulo,
        "antepenultimoarticulo": antepenultimo_articulo,
        "mostrar_pagina2": mostrar_pagina2, 
    }

    if len(articulos) == 0:
        context["mensaje"] = "No existen artículos aún"

    return render(request, "blog_app/inicio.html", context)



def sobre_autor(request): 
    nombre = "Lucas Iaccarino"
    foto = "Blog\Blog\media\Foto_Lucas.jpeg"
    descripcion = "Este es mi primer trabajo practico como programador de Python y Django. \n Me interesa aprender sobre nuevas técnicas y poder implementarlas en mi trabajo"
    context = {"nombre":nombre, "descripcion": descripcion}
    return render(request, "blog_app/sobre_autor.html", context)

def agregar_imagen(request):
  if request.method == "POST":
      formulario = ImagenFormulario(request.POST, request.FILES) 

      if formulario.is_valid():
          imagen = formulario.save()
          imagen.articulo = request.articulo
          imagen.save()
          url_exitosa = reverse('inicio')
          return redirect(url_exitosa)
  else:  # GET
      formulario = ImagenFormulario()
  return render(
      request=request,
      template_name="blog_app/formulario_imagen.html",
      context={'form': formulario},
      )


# Create your views here.
