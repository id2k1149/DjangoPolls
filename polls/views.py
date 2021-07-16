from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
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


# class QuestionDetailView(DetailView):
#     model = Question
#     template_name = 'polls/detail.html'

def question_detail_view(request, pk):
    question = get_object_or_404(Question, id=pk)
    max_votes_answer = question.answers.order_by('-votes').first()
    if max_votes_answer.votes == 0:
        max_votes_answer = ''

    voter = Record()
    voter.user = request.user
    voter.question = question
    if voter.voted_already():
        # return HttpResponse('Вы уже голосовали в этом опросе')
        return render(request, 'polls/each_question.html', {
            'question': question,
            'error_message': "You already voted",
            'max_votes_answer': max_votes_answer,
        })
    else:
        return render(request, 'polls/each_question.html', {
            'question': question,
            'max_votes_answer': max_votes_answer,
        })


def vote(request, poll_id):
    question = get_object_or_404(Question, pk=poll_id)
    if not question.is_active:
        return HttpResponse('Sorry, this question is not actual now')

    voter = Record()
    voter.user = request.user
    voter.question = question
    if voter.voted_already():
        # return HttpResponse('Вы уже голосовали в этом опросе')
        return render(request, 'polls/each_question.html', {
            'question': question,
            'error_message': "You already voted",
        })

    if request.POST.get('answer'):
        try:
            selected_answer = question.answers.get(pk=request.POST['answer'])
        except (question.answers.get(pk=request.POST['answer']).DoesNotExist,
                UnicodeEncodeError,
                ValueError):
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "Invalid answer",
            })
        selected_answer.votes += 1
        selected_answer.save()

        voter.answer = selected_answer
        voter.save()

        return HttpResponseRedirect(reverse('polls:best', args=(question.id,)))
    else:
        return render(request, 'polls/each_question.html', {
            'question': question,
            'error_message': "Please, choose an answer",
        })


class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'


def best_result(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    max_votes_answer = question.answers.order_by('-votes').first()

    return render(request, 'polls/best.html', {
        'question': question,
        'max_votes_answer': max_votes_answer,
    })
