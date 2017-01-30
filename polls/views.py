from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello.")
    
def details(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")
    
def results(request, question_id):
    return HttpResponse(f"You're looking at results for question {question_id}")
    
def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
