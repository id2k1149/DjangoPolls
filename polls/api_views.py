from .models import Question, Answer, VoteCounter
from .serializers import QuestionSerializer, AnswerSerializer, VoteSerializer
from rest_framework import viewsets


# ViewSets define the view behavior.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.prefetch_related('answers')
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class VoteViewSet(viewsets.ModelViewSet):
    queryset = VoteCounter.objects.all()
    serializer_class = VoteSerializer
