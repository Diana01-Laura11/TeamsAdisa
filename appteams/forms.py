from django import forms
from .models import cedulas,arbitros,equipos,League,Play,jugadores,estadios,coachs

class cedulas(forms.ModelForm):
    class Meta:
        model = cedulas
        fields = ["name","play_id","playera_id","play_desc","resultado","fecha_inicio","fecha_fin","state"]

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
        fields = ["name","foto","cant_teams"]

class Play(forms.ModelForm):
    class Meta:
        model = Play
        fields = ["folio","fecha","liga","status_play"]

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


