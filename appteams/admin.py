from django.contrib import admin
from .models import cedulas,arbitros,equipos,League,Play,jugadores,estadios,poblaciones,coachs

# Register your models here.
admin.site.register(cedulas)
admin.site.register(arbitros)
admin.site.register(League)
admin.site.register(Play)
admin.site.register(equipos)
admin.site.register(jugadores)
admin.site.register(estadios)
admin.site.register(poblaciones)
admin.site.register(coachs)

