from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

class IndexView(generic.ListView):
  # ListView is a generic view for viewing a list of items.
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions -- not including those set to be published in future!"""
        return Question.objects.filter(
          pub_date__lte=timezone.now()
          # pub_date less than or equal to now
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
  # DetailView is a generic view for showing the details of a particular item
    model = Question
    
    # By default, the DetailView generic view uses a template called <app name>/<model name>_detail.html
    # so normally it would look for polls/question_detail.html, but we'll use polls/detail.html instead since we already made that
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
      # this is a custom method that i guess overrides the default get_queryset behavior
        """
        excludes questions that aren't published yet so they can't be accessed by direct URL
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # request.POST is a dictionary-like object that lets you access submitted data by key name. In this case, request.POST['choice'] returns the ID of the selected choice, as a string. request.POST values are always strings.
        # request.POST['choice'] will raise KeyError if choice wasn???t provided in POST data. The above code checks for KeyError and redisplays the question form with an error message if choice isn???t given
    except (KeyError, Choice.DoesNotExist):
      # re-display the question voting form
      return render(request, 'polls/detail.html',{
        'question': question,
        'error_message': "You must select a choice."
      })
    else: 
      selected_choice.votes +=1
      selected_choice.save()
      # note this^ can result in a race condition if two users vote simultaneously
      #always return HttpResponseRedirect after dealing with POST data to avoid BACK button posting data 2x
      #  HttpResponseRedirect takes a single argument: the URL to which the user will be redirected
      return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
      # reverse() takes the name of the view that we want to pass control to (polls:results)
      # so this would result in a path like /polls/:questionId/results/
      
def new(req):
  # this is called when user clicks "submit" on the add new poll form
  try:
    text = req.POST['question_text']
    dt = req.POST['pub_date']
    newQuestion = Question(question_text=text,pub_date=timezone.now())
    newQuestion.save()
    choiceOne = Choice(question=newQuestion, choice_text=req.POST['choice_one_text'])
    choiceTwo = Choice(question=newQuestion, choice_text=req.POST['choice_two_text'])
    choiceOne.save()
    choiceTwo.save()
  except(KeyError):
    return render(req, 'polls/add=question.html',{'error_message':"something went wrong"})
  else:
    print(req)
    return HttpResponseRedirect('/polls/')

def add_question(req):
  return render(req, 'polls/add-question.html')
