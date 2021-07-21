from django.urls import path
from polls import views
from django.contrib.auth.views import LogoutView

app_name = 'polls'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('questions/', views.QuestionsListView.as_view(), name='questions'),
    # path('questions/', views.questions_list_view, name='questions'),
    path('<int:question_id>/', views.question_detail_view, name='question'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/result/', views.result, name='result'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('poll/', views.add_poll, name='poll'),
    path('newpoll/', views.new_poll, name='newpoll'),
    path('update/', views.update, name='update'),

]
