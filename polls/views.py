from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Question

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {
      'latest_question_list': latest_questions
    }
    return render(request, 'polls/index.html', context)
    
def details(request, question_id):
    try:
      question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
      raise Http404("Question does not exist")
    return render(request, 'polls/details.html', {'question': question})
    
def results(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    
def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    choice_id = request.POST["choice"]
    
    choice = question.choice_set.get(pk=choice_id)
    choice.votes += 1
    choice.save()
    
    return HttpResponseRedirect(reverse('results', args=(question.id,)))
