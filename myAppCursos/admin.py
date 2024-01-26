from django.contrib import admin
from .models import Curso


class CursoAdmin(admin.ModelAdmin): 
    search_fields = ('nombre',)
    
admin.site.register(Curso, CursoAdmin)
