from django.shortcuts import render # Esto ha sido comentado en cuanto a a la versión original

# Create your views here.

from django.http import HttpResponse

# from django.http import HttpResponse

from .models import Question


#def index(request):
#    return HttpResponse("Hola a todos, tu estas en el indice de pools.")

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("Tu estas viendo la encuesta %s." % question_id)

def results(request, question_id):
    response = "Tu estas viendo el resultado de la encuesta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Tu estas votando en una encuesta %s." % question_id)
