from django.shortcuts import render
from .models import Question
from django.http import Http404


# Create your views here.
from django.http import HttpResponse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    # note the render() shortcut method above
    # args: request object, template name, dictionary(optional)

def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist. 404.")
  return render(request, "polls/detail.html", {'question':question})
  
def results(request, question_id):
  response="You're looking at the results of question %s."
  return HttpResponse(response % question_id)
  # I'm not really sure why we're interpolating the variables differently in detail vs. results, i think just for demonstration purposes.

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)
  

