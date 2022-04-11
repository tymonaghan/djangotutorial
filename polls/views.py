from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.
from django.http import HttpResponse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    # note the render() shortcut method above
    # args: request object, template name, dictionary(optional)

def detail(request, question_id):
  # get_object_or_404 replaces a try/except block
  # use get_list_or_404 if you want to return a list (use filter() instead of get()), which will still raise Http404 if the list is empty.
  question = get_object_or_404(Question, pk=question_id)
  return render(request, "polls/detail.html", {'question':question})
  
def results(request, question_id):
  response="You're looking at the results of question %s."
  return HttpResponse(response % question_id)
  # I'm not really sure why we're interpolating the variables differently in detail vs. results, i think just for demonstration purposes.

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)
  

