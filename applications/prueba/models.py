from django.db import models

# Create your models here.
class Prueba(models.Model):
    Archivo = models.CharField('Archivo', max_length=50)
    Documento = models.FileField('Documento', upload_to=None, max_length=100)

    class Meta:
        """Meta definition for Prueba."""

        verbose_name = 'Prueba'
        verbose_name_plural = 'Pruebas'

    def __str__(self):
        return self.Archivo
