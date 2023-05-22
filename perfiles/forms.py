from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from perfiles.models import Avatar

class UserRegisterForm(UserCreationForm):
   #
   password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
   password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

   class Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):

   class Meta:
       model = User
       fields = ["email"]
       

class AvatarFormulario(forms.ModelForm):

   class Meta:
       model = Avatar
       fields = ['imagen']      