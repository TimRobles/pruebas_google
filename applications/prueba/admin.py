from django.contrib import admin

from .models import Prueba

# Register your models here.
class PruebaAdmin(admin.ModelAdmin):
    '''Admin View for Prueba'''

    list_display = (
        'Archivo',
        'Documento',
        )
    
admin.site.register(Prueba, PruebaAdmin)