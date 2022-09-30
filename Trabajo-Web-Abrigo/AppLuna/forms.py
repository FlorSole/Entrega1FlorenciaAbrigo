from django import forms


class DuenoFormulario(forms.Form):

    nombre = forms.CharField(max_length=60)
    edad = forms.IntegerField()
    
    


class PerroFormulario(forms.Form):

    nombre = forms.CharField(max_length=60)
    raza = forms.CharField(max_length=60)
    sexo = forms.CharField(max_length=60)
    edad = forms.IntegerField()

class GatoFormulario(forms.Form):

    nombre = forms.CharField(max_length=60)
    raza = forms.CharField(max_length=60)
    sexo = forms.CharField(max_length=60)
    edad = forms.IntegerField()

class RoedorFormulario(forms.Form):

    nombre = forms.CharField(max_length=60)
    raza = forms.CharField(max_length=60)
    sexo = forms.CharField(max_length=60)
    edad = forms.IntegerField()