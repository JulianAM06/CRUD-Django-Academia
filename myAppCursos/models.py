from django.db import models

class Curso(models.Model):
    
    idCurso = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    creditos = models.SmallIntegerField()
    
    def __str__(self):
        return ("Curso: " + self.nombre + " (" + str(self.creditos) + ")")
