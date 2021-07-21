from django.db import models
from datetime import date
from django.contrib.auth.models import User


# Create your models here.
class Answer(models.Model):
    answer = models.CharField(max_length=64)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.answer


class Question(models.Model):
    title = models.CharField(max_length=128, verbose_name="Question", default='Where to have a lunch?')
    date_published = models.DateField(default=date.today)
    answers = models.ManyToManyField(Answer)
    result = models.CharField(max_length=64,
                              blank=True,
                              null=True,
                              verbose_name="Result")

    def __str__(self):
        return self.title


class Info(models.Model):
    text = models.CharField(max_length=64, unique=False)

    def __str__(self):
        return self.text


class Description(models.Model):
    date_published = models.DateField(default=date.today)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    text_info = models.ForeignKey(Info, on_delete=models.CASCADE)
    digital_info = models.DecimalField(decimal_places=2, default=0, max_digits=5)


class VotesCounter(models.Model):
    answer = models.ForeignKey(Answer,
                               on_delete=models.CASCADE,
                               verbose_name="Answer")
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 verbose_name="Question",
                                 related_name='question_votes_counters'
                                 )
    votes = models.IntegerField(verbose_name="Votes", default=0)

    def __str__(self):
        return self.answer.answer


class Voter(models.Model):
    date = models.DateField(default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 verbose_name='Question')

    answer = models.ForeignKey(VotesCounter, on_delete=models.CASCADE, verbose_name='Answer')

    def __str__(self):
        return self.user.username

    def voted_already(self):
        user_list = Voter.objects.filter(user=self.user, question=self.question)
        return len(user_list) > 0
