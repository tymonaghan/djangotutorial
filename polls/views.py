from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

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
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', {'question':question}) # so remember, it's request object, template name, optional dictionary. so polls/results.html is the template in this case.

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # request.POST is a dictionary-like object that lets you access submitted data by key name. In this case, request.POST['choice'] returns the ID of the selected choice, as a string. request.POST values are always strings.
        # request.POST['choice'] will raise KeyError if choice wasn’t provided in POST data. The above code checks for KeyError and redisplays the question form with an error message if choice isn’t given
    except (KeyError, Choice.DoesNotExist):
      # re-display the question voting form
      return render(request, 'polls/detail.html',{
        'question': question,
        'error_message': "You must select a choice."
      })
    else: 
      selected_choice.votes +=1
      selected_choice.save()
      #always return HttpResponseRedirect after dealing with POST data to avoid BACK button posting data 2x
      #  HttpResponseRedirect takes a single argument: the URL to which the user will be redirected
      return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
      # reverse() takes the name of the view that we want to pass control to (polls:results)
      # so this would result in a path like /polls/:questionId/results/
