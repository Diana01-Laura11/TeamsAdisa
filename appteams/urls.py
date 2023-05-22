from django.urls import path
from . import views


urlpatterns = [
    path('', views.estadios_view),
    path('registrar-cedula/', views.cedulas_view),
    path('registrar-arbitro/', views.arbitros_view),
    path('registrar-equipo/', views.equipos_view),
    path('registrar-League/', views.League_view),
    path('registrar-estadio/', views.estadios_view),
    path('registrar-Play/', views.Play_view),
    path('registrar-coach/', views.coachs_view),
    path('registrar-jugador/', views.jugadores_view),
    path('equipos/',views.ver_equipos),
    path('cedulas/',views.ver_cedulas),
]