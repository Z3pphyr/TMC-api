from django.db import models
from django.utils import timezone
import datetime


class Cliente( models.Model ):
    id = models.AutoField( primary_key = True )
    nombre = models.CharField( max_length = 100, blank = False, null = False )
    direccion = models.CharField( max_length = 100, blank = False, null = False )
    ciudad = models.CharField( max_length = 50, blank = False, null = False)
    comuna = models.CharField( max_length = 50)
    telefono = models.CharField( max_length = 9 )
    correo =  models.EmailField( max_length = 50 )

    def __str__( self ):
        return self.nombre

class Tecnico( models.Model ):
    id = models.AutoField( primary_key = True )
    nombre = models.CharField(  max_length = 100, blank = False, null = False )
    cliente = models.ManyToManyField( Cliente )
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 50)

    def __str__( self ):
        return self.nombre

class Orden( models.Model ):
    folio = models.AutoField( primary_key = True )
    cliente =models.ManyToManyField( Cliente )
    fecha = models.DateField( default= datetime.date.today, blank = False, null = False )
    descripcion = models.TextField( max_length = 200, blank = True, null = True )
    tecnico =models.ManyToManyField( Tecnico )

    def __str__( self ):
        return str( self.folio )
