from django import forms
#from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Articulo, Avatar, Comentario

class CrearAvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['image']

class CrearUsuarioForm(UserCreationForm):
 class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre/s',
            'last_name': 'Apellido/s',
            'email': 'Email',
            'password1': 'Ingresa la Contraseña',
            'password2': 'Confirmar la Contrañea',
    }
    widgets = {
        'username': forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Nombre de Usuario',
            }
        ),
        'first_name': forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Nombre/s',
            }
            ),
        'last_name': forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Apellido/s',
            }
            ),
        'email': forms.EmailInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Email',
            }
            ),
        'password1': forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '',
            }
            ),
        'password2': forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '',
            }
            ),
    }
class CrearArticuloForm(forms.ModelForm):
    class Meta:
     model = Articulo
     fields = ['titulo', 'contenido', 'imagen', 'autor']
     labels = {
            'titulo': 'Titulo del articulo',
            'contenido': 'Contenido del articulo',
            'imagen': 'Ingrese link de la imagen',
            'autor': 'Autor',
    }

class ArticuloSearchForm(forms.Form):
    titulo = forms.CharField(
        max_length=50, required=True, label="Ingrese titulo del articulo"
    )

class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class CrearComentarioForm(forms.ModelForm):
  class Meta:
    model = Comentario
    fields = ['nom_usr', 'contenido', 'activo']
    labels = {
            'nom_usr': 'Nombre de Usuario',
            'contenido': 'Comentario',
            'activo': 'Activo',       
    }
