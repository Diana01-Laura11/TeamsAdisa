from django.urls import path
from . import views


urlpatterns = [
    path('cedulas/', views.cedulas_view),
    path('arbitros/', views.arbitros_view),
    path('equipos/', views.equipos_view),
    path('League/', views.League_view),
    path('estadios/', views.estadios_view),
    path('Play/', views.Play_view),
    path('coachs/', views.coachs_view),
    path('jugadores/', views.jugadores_view)
]