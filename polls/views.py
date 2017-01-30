from django.shortcuts import render
from django.http import HttpResponse, Http404

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
    return HttpResponse(f"You're looking at results for question {question_id}")
    
def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
