from django.db import models

# Create your models here.
class Tareas(models.Model):
    estados = [('termiando', 'tarea terminada, bien echo'),
               ('incompleto','tarea incompleta, mal echo')
               ]
    titulo = models.CharField(max_length=100)
    descripcion =(models.TextField(max_length=500))
    estados = models.CharField(choices=estados,default='incompleto')
    def __str__(self):
        return self.titulo