from django.urls import path
from polls import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.QuestionDetailView.as_view(), name='detail'),
    path('<int:pk>/', views.question_detail_view, name='each_question'),
    path('<int:poll_id>/vote/', views.vote, name='vote'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/best/', views.best_result, name='best')
]
