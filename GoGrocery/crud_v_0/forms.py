from django import forms
from .models import Usuario

class loggin_form(forms.Form):
    username = Usuario.nickname
    password = Usuario.contrasenia