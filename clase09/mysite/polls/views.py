#from django.shortcuts import render

# Agregados del tutorial

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola a todos, tu estas en el indice de polls")
