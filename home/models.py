from django.db import models

# Create your models here.
class Home(models.Model):
    Encabezado = models.CharField('Encabezado', max_length=100)

    def __str__(self):
        return self.Encabezado

    class Meta:
        verbose_name = "Encabezado"
        verbose_name_plural = "Encabezado"
        ordering = ['Encabezado']