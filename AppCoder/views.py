from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiante

# Create your views here.
def curso(self):

    curso = Curso(nombre="Desarrollo Web", camada="19881")
    curso.save()
    documentoDeTexto = f"--->Curso: {curso.nombre}  Camada: {curso.camada}"

    return HttpResponse(documentoDeTexto)

def estudiante(self):

    estudiante = Estudiante(nombre="Daniel", apellido="Dose", email="dani.ush.14@gmail.com")
    estudiante.save()
    documentoDeTexto = f"--->Estudiante: {estudiante.nombre} _ {estudiante.apellido}    E-Mail: {estudiante.email}"

    return HttpResponse(documentoDeTexto)