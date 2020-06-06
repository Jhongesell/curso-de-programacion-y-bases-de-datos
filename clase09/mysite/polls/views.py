#from django.shortcuts import render

# Agregados del tutorial

#from django.http import HttpResponse #temporal
#from django.template import loader #temporal

from django.shortcuts import render # agregado

from .models import Question

#def index(request):
#return HttpResponse("Hola a todos, tu estas en el indice de polls")

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

#def detail(request, question_id):
 #   return HttpResponse("Tu estas viendo la consulta %s." % question_id)

def results(request, question_id):
    response = "Tu estas viendo el resultado de la consulta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Tu estas votando por la consulta %s." % question_id)

def detail(request, question_id):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Consulta no existente")
    return render(request, 'polls/detail.html', {'question': question})
