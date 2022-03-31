from django.contrib import admin

# Register your models here.
class PruebaAdmin(admin.ModelAdmin):
    '''Admin View for Prueba'''

    list_display = (
        'Archivo',
        'Documento',
        )
    
admin.site.register(Admin, PruebaAdmin)