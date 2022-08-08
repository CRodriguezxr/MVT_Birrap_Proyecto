from django import forms



class Formulario_birras(forms.Form):
    name = forms.CharField (max_length=50)
    style = forms.CharField (max_length=50)
    alcohol_volume = forms.FloatField ()
    IBU = forms.FloatField ()
    description = forms.CharField (max_length=2500)
    malt = forms.CharField (max_length=50,)
    hop = forms.CharField (max_length=50)
    price = forms.FloatField ()
    creation_date = forms.DateField ()
    is_active = forms.BooleanField ()