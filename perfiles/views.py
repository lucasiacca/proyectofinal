from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required

from perfiles.forms import UserRegisterForm, UserUpdateForm, AvatarFormulario


def registro(request):
   if request.method == "POST":
       formulario = UserRegisterForm(request.POST)

       if formulario.is_valid():
           formulario.save()  
           url_exitosa = reverse('inicio')
           return redirect(url_exitosa)
   else:  # GET
       formulario = UserRegisterForm()
   return render(
       request=request,
       template_name='perfiles/registro.html',
       context={'form': formulario},
   )

def login_view(request):
    next_url = request.GET.get("next")
    if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)

       if form.is_valid():
           data = form.cleaned_data
           usuario = data.get('username')
           password = data.get('password')
           user = authenticate(username=usuario, password=password)
           
           if user:
               login(request=request, user=user)
               if next_url:
                   return redirect(next_url)
               url_exitosa = reverse('inicio')
               return redirect(url_exitosa)
    else:  
       form = AuthenticationForm()
    return render(
       request=request,
       template_name='perfiles/login.html',
       context={'form': form},
   )
   
class CustomLogoutView(LogoutView):
       template_name = "perfiles/logout.html"

class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
   form_class = UserUpdateForm
   success_url = reverse_lazy('inicio')
   template_name = 'perfiles/formulario_perfil.html'

   def get_object(self, queryset=None):
       return self.request.user

def agregar_avatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            # Eliminar el avatar existente si existe
            if hasattr(request.user, 'avatar') and request.user.avatar:
                request.user.avatar.delete()
            else:
            # Guardar el nuevo avatar
             avatar = form.save(commit=False)
             avatar.user = request.user
             avatar.save()
             url_exitosa = reverse('editar_perfil')
             return redirect(url_exitosa)
    else:  # GET
        form = AvatarFormulario()
    
    return render(
        request=request,
        template_name="perfiles/formulario_avatar.html",
        context={'form': form}
    )




