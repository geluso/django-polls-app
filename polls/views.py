from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic

from .models import Question

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
    
class DetailsView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    
def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    choice_id = request.POST["choice"]
    
    choice = question.choice_set.get(pk=choice_id)
    choice.votes += 1
    choice.save()
    
    return HttpResponseRedirect(reverse('results', args=(question.id,)))
