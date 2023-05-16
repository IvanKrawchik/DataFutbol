from django.contrib import admin
from .models import Jugadores,Tecnicos,Equipos

# Register your models here.
class JugadoresAdmin(admin.ModelAdmin):
    list_display=('equipo_id','nombre','posicion')

class TecnicosAdmin(admin.ModelAdmin):
    list_display=('equipo_id','nombre')

class EquiposAdmin(admin.ModelAdmin):
    list_display=('equipo_id','nombre')

admin.site.register(Jugadores, JugadoresAdmin)
admin.site.register(Tecnicos, TecnicosAdmin)
admin.site.register(Equipos, EquiposAdmin)