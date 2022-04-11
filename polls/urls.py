from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/ (because this is accessed from ../urls.py which contains the root polls/ route)
    # After finding the match at 'polls/', Django strips off the matching text ("polls/") and sends the remaining text – "34/" – to the ‘polls.urls’ URLconf for further processing: we are here
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
