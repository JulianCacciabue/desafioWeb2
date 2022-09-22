from django import forms


class FormularioInscripcion(forms.Form):

    nombre = forms.CharField()
    edad = forms.IntegerField()
    correo = forms.EmailField()