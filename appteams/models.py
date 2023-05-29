from django.db import models 

#______________________________________________________________
class League(models.Model):
    name = models.CharField(max_length=200,verbose_name="Nombre de la liga")
    foto = models.ImageField(upload_to='images/',verbose_name="Foto")

    def __str__(self):
        return self.name


class poblaciones(models.Model):
    name = models.CharField(max_length=200)
#______________________________________________________________
class coachs(models.Model):  
    name = models.CharField(max_length=200,verbose_name="Nombre del coach")
    photo = models.ImageField(upload_to='images/',default=None,verbose_name="Foto")

    def __str__(self):
        return self.name
#______________________________________________________________
class equipos(models.Model):
    liga_id = models.ForeignKey(League, on_delete=models.SET_NULL,null=True,blank=False,verbose_name="Liga")
    name = models.CharField(max_length=200,verbose_name="Nombre del equipo",null=False,blank=False)
    coach_id = models.ForeignKey(coachs,on_delete=models.SET_NULL,null=True,blank=False,verbose_name="Coach")
    photo = models.ImageField(upload_to='images/',default=None,verbose_name="Foto")
    ##jugadores2_ids = models.ManyToManyField('jugadores',verbose_name="Jugadores")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering=['liga_id','name']
#______________________________________________________________
class jugadores(models.Model):
    team = models.ForeignKey(equipos,on_delete=models.CASCADE,related_name="jugadores_ids",verbose_name="Equipo")
    name = models.CharField(max_length=200,verbose_name="Nombre del jugador")
    photo = models.ImageField(upload_to='images/',default=None,verbose_name="Foto")
    numero = models.IntegerField(verbose_name="Número de la playera")
    pos = [
    ('del','Delantero'),
    ('def','Defensa'),
    ('por','Portero'),
    ('car', 'Carrilero'),
    ('cen', 'Central'),
    ]
    posicion = models.CharField(max_length=3, choices=pos,default='del',verbose_name="Posición")
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        ordering=['team','name']

#______________________________________________________________
class estadios(models.Model):
    liga_id = models.ForeignKey(League, on_delete=models.CASCADE,verbose_name="Liga")
    name = models.CharField(max_length=200,verbose_name="Nombre del estadio")
    photo = models.ImageField(upload_to='images/',verbose_name="Foto del estadio")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Estadio'
        verbose_name_plural = 'Estadios'
        ordering=['liga_id','name']

#______________________________________________________________
class arbitros(models.Model):
    liga_id= models.ForeignKey(League,on_delete=models.CASCADE,verbose_name="Liga")
    name = models.CharField(max_length=200,verbose_name="Nombre del arbitro",)
    photo = models.ImageField(upload_to='images/',verbose_name="Foto")
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Arbitro'
        verbose_name_plural = 'Arbitros'
        ordering=['liga_id','name']

#______________________________________________________________
class Play(models.Model):
    folio = models.CharField(max_length=200,verbose_name="Folio")
    fecha = models.DateTimeField() 
    liga = models.ForeignKey(League,on_delete=models.DO_NOTHING,verbose_name="Liga" )
    team1 = models.ForeignKey(equipos,on_delete=models.SET_NULL, null=True, default=None,related_name='team1_plays',verbose_name="Equipo Local")
    team2 = models.ForeignKey(equipos,on_delete=models.SET_NULL, null=True, default=None,related_name='team2_plays',verbose_name="Equipo Visitante")
    estadio = models.ForeignKey(estadios,on_delete=models.SET_NULL, null=True, default=None,verbose_name="Estadio")

    POSICION_CHOICES = [
        ('cen', 'Central'),
        ('ban', 'Bandera'),
        ('otro', 'Otro')
    ]
    
    arbitro_1 = models.ForeignKey(arbitros, on_delete=models.DO_NOTHING, null=True, default=None, verbose_name="Primer Arbitro", related_name="primer_arbitro")
    posicion_arbitro_1 = models.CharField(max_length=4, choices=POSICION_CHOICES, default='cen',verbose_name="Posición del primer arbitro")
    arbitro_2 = models.ForeignKey(arbitros, on_delete=models.DO_NOTHING, null=True, default=None, verbose_name="Segundo Arbitro", related_name="segundo_arbitro")
    posicion_arbitro_2 = models.CharField(max_length=4, choices=POSICION_CHOICES, default='cen',verbose_name="Posición del segundo arbitro")
    arbitro_3 = models.ForeignKey(arbitros, on_delete=models.DO_NOTHING, null=True, default=None, verbose_name="Tercer Arbitro", related_name="tercer_arbitro")
    posicion_arbitro_3 = models.CharField(max_length=4, choices=POSICION_CHOICES, default='cen',verbose_name="Posición del tercer arbitro")
    arbitro_4 = models.ForeignKey(arbitros, on_delete=models.DO_NOTHING, null=True, default=None, verbose_name="Cuarto Arbitro", related_name="cuarto_arbitro")
    posicion_arbitro_4 = models.CharField(max_length=4, choices=POSICION_CHOICES, default='cen',verbose_name="Posición del cuarto arbitro")
    
    def __str__(self):
        return self.folio
    
        
#_____________________________________________________________
    
class cedulas(models.Model):
    name = models.CharField(max_length=200,verbose_name="Folio",null=False,blank=False)
    play_id = models.ForeignKey(Play,on_delete=models.CASCADE,verbose_name='Juego')
    play_desc = models.CharField(max_length=200,verbose_name="Titulo")
    resultado = models.CharField(max_length=200,verbose_name="Resultado del partido")
    fecha_inicio = models.DateTimeField(null=False,blank=False,verbose_name="Fecha de incio")
    fecha_fin = models.DateField(null=False,blank=False,verbose_name="Fecha de finalización")
    
    def __str__(self):
        return self.name
    
    
    
    
    

