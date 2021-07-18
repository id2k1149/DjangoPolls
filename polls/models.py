from django.db import models
from datetime import date
from django.contrib.auth.models import User


# Create your models here.
class Answer(models.Model):
    answer = models.CharField(max_length=64)

    def __str__(self):
        return self.answer


class Description(models.Model):
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    description = models.CharField(max_length=64, unique=False)
    digital_info = models.DecimalField(decimal_places=2, default=0, max_digits=5)

    def __str__(self):
        return self.description


class Question(models.Model):
    title = models.CharField(max_length=128, verbose_name="Question", default='Where to have a lunch?')
    date_published = models.DateField(default=date.today)
    result = models.ForeignKey(Answer,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               verbose_name="Result")

    def __str__(self):
        return self.title


class VotesCounter(models.Model):
    answer_id = models.OneToOneField(Answer,
                                     on_delete=models.CASCADE,
                                     verbose_name="Answer")
    question_id = models.ForeignKey(Question,
                                    on_delete=models.CASCADE,
                                    verbose_name="Question")
    votes = models.IntegerField(verbose_name="Votes", default=0)

    def __str__(self):
        return self.answer_id.answer



class Voter(models.Model):
    date = models.DateField(default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Question')
    answer = models.ForeignKey(VotesCounter, on_delete=models.CASCADE, verbose_name='Answer')

    def __str__(self):
        return self.user.username

    def voted_already(self):
        user_list = Voter.objects.filter(user=self.user, question=self.question)
        return len(user_list) > 0
