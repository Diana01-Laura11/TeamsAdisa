from django.urls import path
from . import views

app_name="appteams"
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
    path('jugadores/',views.ver_jugadores),
    path('eliminar_jugador/<int:id>', views.eliminarJugador, name= 'eliminar_jugador')
]