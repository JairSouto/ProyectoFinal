from django import forms

class EquiposFormularios(forms.Form):
    nombre=forms.CharField(max_length=30)

    seguidores=forms.IntegerField()
class AsociadosFormularios(forms.Form):
    nombre=forms.CharField(max_length=30)
    redes_sociales=forms.CharField(max_length=30)
class CursosFormularios(forms.Form):
        nombre=forms.CharField(max_length=50)
        jugadorpro=forms.CharField(max_length=40)
        duracion=forms.CharField(max_length=40)