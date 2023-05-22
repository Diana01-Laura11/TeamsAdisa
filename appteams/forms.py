from django import forms
from .models import cedulas,arbitros,equipos,League,Play,jugadores,estadios,coachs
from django.contrib.admin import widgets

class cedulas(forms.ModelForm):
    fecha_inicio=forms.DateTimeField(
        label='Fecha Inicio',
        widget=forms.DateTimeInput(attrs={'class': 'datetimepicker', 'type': 'datetime-local'}),)
    fecha_fin=forms.DateTimeField(
        label='Fecha Fin',
        widget=forms.DateTimeInput(attrs={'class': 'datetimepicker', 'type': 'datetime-local'}),)
    class Meta:
        model = cedulas
        fields = ["name","play_id","play_desc","resultado","fecha_inicio","fecha_fin"]

class arbitros(forms.ModelForm):
    class Meta:
        model = arbitros
        fields = ["liga_id","name","photo"]

class equipos(forms.ModelForm):
    class Meta:
        model = equipos
        fields = ["liga_id","name","coach_id"]
        
class League (forms.ModelForm):
    class Meta:
        model = League
        fields = ("name","foto")

class Play(forms.ModelForm):
    fecha = forms.DateTimeField(
        label='Fecha',
        widget=forms.DateTimeInput(attrs={'class': 'datetimepicker', 'type': 'datetime-local'}),)
    class Meta:
        model = Play
        fields = ["folio","fecha","liga","team1","team2","estadio","arbitro","posicion"]
        
    

class jugadores(forms.ModelForm):
    class Meta:
        model = jugadores
        fields = ["team","name","photo","numero","posicion"]

class estadios(forms.ModelForm):
    class Meta:
        model = estadios
        fields = ["liga_id","name","photo"]

class coachs(forms.ModelForm):
    class Meta:
        model = coachs
        fields = ["name","photo"]    


