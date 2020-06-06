#from django.shortcuts import render # Esto ha psido comentado en cuanto a a la versión original
#from django.shortcuts import get_object_or_404, render

# Create your views here.

#from django.http import HttpResponse
#from django.http import HttpResponse, HttpResponseRedirect


#from django.http import Http404

# from django.http import HttpResponse

#from .models import Question

#from django.template import loader

# Parte 04 de la guía:


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question

#def index(request):
#    return HttpResponse("Hola a todos, tu estas en el indice de pools.")

#def index(request):
 #   latest_question_list = Question.objects.order_by('-pub_date')[:5]
  #  output = ', '.join([q.question_text for q in latest_question_list])
   # return HttpResponse(output)

#def index(request):
 #   latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
  #  template = loader.get_template('polls/index.html')
   # context = {
    #    'latest_question_list': latest_question_list,
     #   }
#    return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
        }
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

#def detail(request, question_id):
 #   return HttpResponse("Tu estas viendo la encuesta %s." % question_id)


#def detail(request, question_id):
 #   try:
  #      question = Question.objects.get(pk=question_id)
   # except Question.DoesNotExist:
    #    raise Http404("La consulta no existe")
#    return render(request, 'polls/detail.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

"""def results(request, question_id):
    response = "Tu estas viendo el resultado de la encuesta %s."
    return HttpResponse(response % question_id)"""

#Parte 04 de la guía
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    #return HttpResponse("Tu estas votando en una encuesta %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Resdisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
