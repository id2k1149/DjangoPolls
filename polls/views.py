from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from datetime import date, datetime
from .models import Question, Voter, VoteCounter, Answer
from .forms import RegistrationForm, QuestionForm, AnswerForm


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
    max_votes_answer = question.answers.order_by('-votes').first()
    if max_votes_answer.votes == 0:
        max_votes_answer = ''

    voter = Voter()
    voter.user = request.user
    voter.question = question
    if voter.voted_already():
        return render(request, 'polls/question.html', {
            'question': question,
            'error_message': "You already voted",
            'max_votes_answer': max_votes_answer,
        })
    else:
        return render(request, 'polls/question.html', {
            'question': question,
            'max_votes_answer': max_votes_answer,
        })


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    if request.POST.get('answer'):
        try:
            selected_answer = question.answers.get(id=request.POST['answer'])
        except (question.answers.get(id=request.POST['answer']).DoesNotExist,
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
            answer_to_change = question.answers.get(id=voter_to_change.answer.id)
            answer_to_change.votes -= 1
            answer_to_change.save()
            voter_to_change.answer = selected_answer
            voter_to_change.save()
        else:
            voter.answer = selected_answer
            voter.save()

        max_votes_answer = question.answers.order_by('-votes').first()
        question.result = max_votes_answer.answer_id
        question.save()

        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
    else:
        max_votes_answer = question.answers.order_by('-votes').first()
        return render(request, 'polls/question.html', {
            'question': question,
            'error_message': "Please, choose an answer",
            'max_votes_answer': max_votes_answer,
        })


@login_required
def result(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    max_votes_answer = question.answers.order_by('-votes').first()

    return render(request, 'polls/result.html', {
        'question': question,
        'max_votes_answer': max_votes_answer,
    })


# CreateView
class AnswerCreateView(LoginRequiredMixin, CreateView):
    fields = ('answer',)
    model = Answer
    success_url = reverse_lazy('polls:questions')
    template_name = 'polls/add_answer.html'

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)


@login_required
def add_poll(request):
    if request.method == 'GET':
        form = QuestionForm()
        return render(request, 'polls/add_poll.html', context={'form': form})
    else:
        form = QuestionForm(request.POST, files=request.FILES)
        if form.is_valid():
            answers = VoteCounter.objects.all()
            for answer in answers:
                answer.votes = 0
                answer.save()
            form.save()
            return HttpResponseRedirect(reverse('polls:questions'))
        else:
            return render(request, 'polls/add_poll.html', context={'form': form})


@login_required
def add_answer(request):
    if request.method == 'GET':
        form = AnswerForm()
        return render(request, 'polls/add_poll.html', context={'form': form})
    else:
        form = QuestionForm(request.POST, files=request.FILES)
        if form.is_valid():
            answers = VoteCounter.objects.all()
            for answer in answers:
                answer.votes = 0
                answer.save()
            form.save()
            return HttpResponseRedirect(reverse('polls:questions'))
        else:
            return render(request, 'polls/add_poll.html', context={'form': form})
