from django.urls import path

from . import views

# Esto fue modificado también el tutorial 1 parte 3
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/9000
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/9000/results
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/9000/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # the 'name' value as called by the {% url %} template tag
    path('<int:question_id>/', views.detail, name='detail'),

    # added the word 'specifics'
    path('specifics/<int:question_id>/', views.detail, name='detail'),
]
# Esto fue agregado en el 90% del tutorial N01 parte 3
app_name = 'polls'
urlpattern = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id/vote/', views.vote, name='vote'),
    ]

