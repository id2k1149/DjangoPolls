from .models import Question, Answer, VoteCounter
from rest_framework import serializers


# Serializers define the API representation.
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VoteCounter
        fields = '__all__'
