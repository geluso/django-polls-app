from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    questions = []
    for question in latest_questions:
      questions.append(question.question_text)
    text = ", ".join(questions)
    return HttpResponse(text)
    
def details(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")
    
def results(request, question_id):
    return HttpResponse(f"You're looking at results for question {question_id}")
    
def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
