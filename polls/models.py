from django.db import models
from datetime import date
from django.contrib.auth.models import User


# Create your models here.
class Diner(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Answer(models.Model):
    diner_id = models.OneToOneField(Diner, on_delete=models.CASCADE)
    votes = models.IntegerField(verbose_name="Votes", default=0)

    def __str__(self):
        return self.diner_id.name


class Question(models.Model):
    title = models.CharField(max_length=128, verbose_name="Question", default='Where to have a lunch?')
    date_published = models.DateField(default=date.today)
    answers = models.ManyToManyField(Answer)
    result = models.ForeignKey(Diner,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               verbose_name="Result")

    def __str__(self):
        return self.title


class Description(models.Model):
    diner_id = models.ForeignKey(Diner, on_delete=models.CASCADE)
    description = models.CharField(max_length=64, unique=False)
    digital_info = models.DecimalField(decimal_places=2, default=0, max_digits=5)

    def __str__(self):
        return self.description


class Record(models.Model):
    date = models.DateField(default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Question')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, verbose_name='Answer')

    def __str__(self):
        return self.user.username

    def voted_already(self):
        user_list = Record.objects.filter(user=self.user, question=self.question)
        return len(user_list) > 0
