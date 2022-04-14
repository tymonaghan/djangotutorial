from django.urls import path

from . import views

app_name = 'polls'
# namespacing as above allows multiple apps to avoid collisions
urlpatterns = [
    # ex: /polls/ (because this is accessed from ../urls.py which contains the root polls/ route)
    # After finding the match at 'polls/', Django strips off the matching text ("polls/") and sends the remaining text – "34/" – to the ‘polls.urls’ URLconf for further processing: we are here
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #The DetailView generic view expects the primary key value captured from the URL to be called "pk"
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('add-question/', views.add_question, name="add-question"),
    path('/new/', views.new, name='new')
]
