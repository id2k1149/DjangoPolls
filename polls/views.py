import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from datetime import date, datetime
from random import randrange
from .models import Question, Voter, VotesCounter, Answer, Description, Info
from .forms import RegistrationForm, QuestionForm


# Create your views here.
def main_view(request):
    return render(request, 'polls/index.html')


class UserLoginView(LoginView):
    template_name = 'polls/login.html'


class UserCreateView(CreateView):
    model = User
    template_name = 'polls/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('polls:login')


class QuestionsListView(LoginRequiredMixin, ListView):
    template_name = 'polls/questions.html'
    context_object_name = 'we_have_questions'

    def get_queryset(self):
        """Return filtered questions"""
        if datetime.now().hour < 23:
            questions = Question.objects \
                .filter(date_published=date.today()) \
                .order_by('-date_published')
            return questions


@login_required
def question_detail_view(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    voter = Voter()
    voter.user = request.user
    voter.question = question
    if voter.voted_already():
        return render(request, 'polls/question.html', {
            'question': question,
            'error_message': "You already voted",

        })
    else:
        return render(request, 'polls/question.html', {
            'question': question,

        })


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    if request.POST.get('answer'):
        try:
            selected_answer = question.question_votes_counters.get(id=request.POST['answer'])
        except (question.question_votes_counters.get(id=request.POST['answer']).DoesNotExist,
                UnicodeEncodeError,
                ValueError):
            return render(request, 'polls/question.html', {
                'question': question,
                'error_message': "Invalid answer",
            })

        selected_answer.votes += 1
        selected_answer.save()

        voter = Voter()
        voter.user = request.user
        voter.question = question
        if voter.voted_already():
            voter_to_change = Voter.objects.get(user=request.user, question=question)
            answer_to_change = question.question_votes_counters.get(id=voter_to_change.answer.id)
            answer_to_change.votes -= 1
            answer_to_change.save()
            voter_to_change.answer = selected_answer
            voter_to_change.save()
        else:
            voter.answer = selected_answer
            voter.save()

        max_votes_answer = question.question_votes_counters.order_by('-votes').first()
        question.result = max_votes_answer.answer.answer
        question.save()

        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
    else:
        max_votes_answer = question.question_votes_counters.order_by('-votes').first()
        return render(request, 'polls/question.html', {
            'question': question,
            'error_message': "Please, choose an answer",
            'max_votes_answer': max_votes_answer,
        })


@login_required
def result(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    max_votes_answer = question.question_votes_counters.order_by('-votes').first()

    return render(request, 'polls/result.html', {
        'question': question,
        'max_votes_answer': max_votes_answer,
    })


@login_required
def new_poll(request):
    if request.method == 'GET':
        form = QuestionForm()
        return render(request, 'polls/newpoll.html', context={'form': form})
    else:
        form = QuestionForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

            question_qs = Question.objects.filter(date_published=date.today())

            for each in question_qs:
                question_pk = each.pk
                question = Question.objects.get(pk=question_pk)
                answers = each.answers.all()

            for each in answers:
                VotesCounter.objects.create(answer=each, question=question)

            return HttpResponseRedirect(reverse('polls:questions'))
        else:
            return render(request, 'polls/newpoll.html', context={'form': form})


@login_required
def update(request):
    answers = Answer.objects.all()
    for each in answers:
        each.is_active = False
        each.save()

    answers = list(answers)
    random_number_1 = randrange(2, len(answers))
    random_answers = random.sample(answers, random_number_1)

    Description.objects.filter(date_published=date.today()).delete()
    for each in random_answers:
        answer_to_change = Answer.objects.get(answer=each)
        answer_to_change.is_active = True
        answer_to_change.save()
        info = list(Info.objects.all())
        random_number_2 = randrange(2, 4)
        random_info = random.sample(info, random_number_2)

        for item in random_info:
            Description.objects.create(answer=each, text_info=item, digital_info=randrange(1, 100))

    today_description = Description.objects.filter(date_published=date.today())

    return render(request, "polls/update.html", context={'today_description': today_description,
                                                         'today_answers': random_answers})
