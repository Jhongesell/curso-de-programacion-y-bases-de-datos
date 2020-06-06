#from django.shortcuts import render

# Agregados del tutorial

from django.http import HttpResponse

from .models import Question

#def index(request):
#return HttpResponse("Hola a todos, tu estas en el indice de polls")

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("Tu estas viendo la consulta %s." % question_id)

def results(request, question_id):
    #response = "You're looking at the results of question %s."
    response = "Tu estas viendo el resultado de la consulta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Tu estas votando por la consulta %s." % question_id)
