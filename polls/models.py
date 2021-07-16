from django.db import models
import datetime
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=128, verbose_name="Question", default='Where to have a lunch?')
    date_published = models.DateTimeField(default=datetime.datetime.now())
    is_active = models.BooleanField(default=True, verbose_name="Active poll")

    def __str__(self):
        return self.title


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=64, verbose_name="Answer")
    votes = models.IntegerField(verbose_name="Votes", default=0)

    def __str__(self):
        return self.answer


class Description(models.Model):
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    description = models.CharField(max_length=64, unique=False)
    digital_info = models.DecimalField(decimal_places=2, default=0, max_digits=5)

    def __str__(self):
        return self.description


class Record(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Question')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, verbose_name='Answer')

    def __str__(self):
        return self.user.username

    def voted_already(self):
        user_list = Record.objects.filter(user=self.user, question=self.question)
        return len(user_list) > 0
