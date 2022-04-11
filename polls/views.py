from django.shortcuts import render
from .models import Question
from django.template import loader


# Create your views here.
from django.http import HttpResponse

def index(request):
  latest_question_list = Question.objects.order_by("-pub_date")[:5]
  template = loader.get_template('polls/index.html')
  context = {
        'latest_question_list': latest_question_list,
    }
  return HttpResponse(template.render(context, request))

def detail(request, question_id):
  return HttpResponse("You're looking at question %s." % question_id)
  
def results(request, question_id):
  response="You're looking at the results of question %s."
  return HttpResponse(response % question_id)
  # I'm not really sure why we're interpolating the variables differently in detail vs. results, i think just for demonstration purposes.

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)
  

