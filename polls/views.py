from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView
from .models import Question, Record
from datetime import date, datetime


# Create your views here.
class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'we_have_questions'

    def get_queryset(self):
        """Return filtered questions"""
        if datetime.now().hour < 23:
            questions = Question.objects \
                .filter(date_published=date.today()) \
                .order_by('-date_published')
            return questions


def question_detail_view(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    max_votes_answer = question.answers.order_by('-votes').first()
    if max_votes_answer.votes == 0:
        max_votes_answer = ''

    voter = Record()
    voter.user = request.user
    voter.question = question
    if voter.voted_already():
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You already voted",
            'max_votes_answer': max_votes_answer,
        })
    else:
        return render(request, 'polls/detail.html', {
            'question': question,
            'max_votes_answer': max_votes_answer,
        })


def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    if request.POST.get('answer'):
        try:
            selected_answer = question.answers.get(id=request.POST['answer'])
        except (question.answers.get(id=request.POST['answer']).DoesNotExist,
                UnicodeEncodeError,
                ValueError):
            return render(request, 'polls/result.html', {
                'question': question,
                'error_message': "Invalid answer",
            })

        selected_answer.votes += 1
        selected_answer.save()

        voter = Record()
        voter.user = request.user
        voter.question = question
        if voter.voted_already():
            voter_to_change = Record.objects.get(user=request.user, question=question)
            answer_to_change = question.answers.get(id=voter_to_change.answer.id)
            answer_to_change.votes -= 1
            answer_to_change.save()
            voter_to_change.answer = selected_answer
            voter_to_change.save()
        else:
            voter.answer = selected_answer
            voter.save()

        max_votes_answer = question.answers.order_by('-votes').first()
        question.result = max_votes_answer.diner_id
        question.save()

        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
    else:
        return render(request, 'polls/result.html', {
            'question': question,
            'error_message': "Please, choose an answer",
        })


def result(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    max_votes_answer = question.answers.order_by('-votes').first()

    return render(request, 'polls/result.html', {
        'question': question,
        'max_votes_answer': max_votes_answer,
    })
