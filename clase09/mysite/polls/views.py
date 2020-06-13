from django.shortcuts import render # agregado

from .models import Question


from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("Tu estas viendo el id: %s." % question_id)

def results(request, question_id):
    response = "Tu estas viendo el resultado de la consulta: %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Tu estas votando en la consulta: %s." % question_id)
