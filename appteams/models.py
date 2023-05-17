from django.db import models 

#______________________________________________________________
class League(models.Model):
    name = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='images/', default=None)
    cant_teams = models.BigIntegerField()

    def __str__(self):
        return self.name


class poblaciones(models.Model):
    name = models.CharField(max_length=200)
#______________________________________________________________
class coachs(models.Model):  
    name = models.CharField(max_length=200,help_text="Ingrese el nombre del coach del equipo")
    photo = models.ImageField(upload_to='images/',default=None)

    def __str__(self):
        return self.name
#______________________________________________________________
class equipos(models.Model):
    liga_id = models.ForeignKey(League, on_delete=models.CASCADE,null=False,blank=False)
    name = models.CharField(max_length=200,verbose_name="Nombre",help_text="Ingrese el nombre del equipo",null=False,blank=False)
    coach_id = models.ForeignKey(coachs,on_delete=models.CASCADE,null=False,blank=False)
    photo = models.ImageField(upload_to='images/',default=None)
    ##jugadores2_ids = models.ManyToManyField(jugadores,on_delete=models.CASCADE,null=False,blank=False)
    
    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering=['liga_id','name']
#______________________________________________________________
class jugadores(models.Model):
    team = models.ForeignKey(equipos,on_delete=models.CASCADE,related_name="jugadores_ids")
    name = models.CharField(max_length=200,help_text="Ingrese el nombre del jugador")
    photo = models.ImageField(upload_to='images/',default=None)
    numero = models.IntegerField(verbose_name="Numero",help_text= "Numero de playera")
    posicion = [
    ('del','Delantero'),
    ('def','Defensa'),
    ('por','Portero'),
    ('car', 'Carrilero'),
    ('cen', 'Central'),
    ]
    posicion = models.CharField(max_length=3, choices=posicion,default='del')
    
    
    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        ordering=['team','name']

#______________________________________________________________
class Play(models.Model):
    folio = models.CharField(max_length=200)
    fecha = models.DateField() 
    liga = models.ForeignKey(League, on_delete=models.CASCADE, default=None, )

    def __str__(self):
        return self.folio
    
    CREADO = 'cre'
    PROGRAMADO = 'prog'
    REALIZADO = 'rea'
    CANCELADO = 'can'

    STATUS_CHOICES = [
        ( CREADO, 'Creado' ),
        ( PROGRAMADO, 'Programado' ),
        ( REALIZADO, 'Realizado' ),
        ( CANCELADO, 'Cancelado' ),
    ]

    status_play = models.CharField(max_length=4, choices=STATUS_CHOICES, default= CREADO)

class Play_Arbitro(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE)

    CENTRAL = 'cen'
    BANDERA = 'ban'
    OTRO = 'otro'

    POSICION_CHOICES = [
        (CENTRAL, 'Central'),
        (BANDERA, 'Bandera'),
        (OTRO, 'Otro')
    ]

    posicion = models.CharField(max_length=4, choices=POSICION_CHOICES, default=CENTRAL)



#______________________________________________________________
class estadios(models.Model):
    liga_id = models.ForeignKey(League, on_delete=models.CASCADE,null=False,blank=False)
    name = models.CharField(max_length=200,help_text="Ingrese el nombre del estadio",null=False,blank=False)
    photo = models.ImageField(upload_to='images/',default=None)
    
    
    class Meta:
        verbose_name = 'Estadio'
        verbose_name_plural = 'Estadios'
        ordering=['liga_id','name']
    
#______________________________________________________________
class arbitros(models.Model):
    liga_id= models.ForeignKey(League,on_delete=models.CASCADE,null=False,blank=False)
    name = models.CharField(max_length=200,help_text="Ingrese el nombre del arbitro",null=False,blank=False)
    photo = models.ImageField(upload_to='images/',default=None)
    
    class Meta:
        verbose_name = 'Arbitro'
        verbose_name_plural = 'Arbitros'
        ordering=['liga_id','name']


        
#_____________________________________________________________
    
class cedulas(models.Model):
    name = models.CharField(max_length=200,verbose_name="Titulo",null=False,blank=False)
    play_id = models.ForeignKey(Play,on_delete=models.CASCADE,verbose_name='Juego')
    playera_id = models.ForeignKey(jugadores, on_delete=models.CASCADE)
    play_desc = models.CharField(max_length=200)
    resultado = models.CharField(max_length=200)
    fecha_inicio = models.DateField(null=False,blank=False)
    fecha_fin = models.DateField(null=False,blank=False)
    state = [
    ('cre','Creado'),
    ('env','Enviada'),
    ('can','Cancelado')
    ]
    state = models.CharField(max_length=3, choices=state,default='cre')
    
    
    
    

