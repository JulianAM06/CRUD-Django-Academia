from django.shortcuts import render, redirect
from .models import Curso

def cursos(request):

    cursos = Curso.objects.all()

    return render(request, 'cursos.html', {'cursos': cursos})

def registrarCurso(request):

    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCredito']

    curso = Curso(idCurso=codigo, nombre=nombre, creditos=creditos)

    curso.save()

    return redirect('/')

def eliminarCurso(request, idCurso):

    curso = Curso.objects.get(idCurso=idCurso)
    curso.delete()

    return redirect('/')

def edicionCurso(request, idCurso):

    curso = Curso.objects.get(idCurso=idCurso)

    return render(request, 'actualizar.html', {'curso': curso})

def editarCurso(request):

    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCredito']

    curso = Curso.objects.get(idCurso=codigo)
    curso.nombre = nombre
    curso.creditos = creditos

    curso.save()

    return redirect('/')

