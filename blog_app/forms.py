from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Imagen

class ImagenFormulario(forms.ModelForm):

   class Meta:
       model = Imagen
       fields = ['imagen']      