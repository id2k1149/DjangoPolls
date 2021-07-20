from django.core.management.base import BaseCommand
from polls.models import Answer, Description, Info
from mixer.backend.django import mixer
import string
import random
from random import randrange


class Command(BaseCommand):

    def handle(self, *args, **options):
        alphabet_list = ('A', 'B', 'C', 'D', 'E', 'F')

        Info.objects.all().delete()
        for each in alphabet_list:
            new_name = 'Food ' + each
            Info.objects.create(text=new_name)

        info = list(Info.objects.all())
        print(info)

        Description.objects.all().delete()
        Answer.objects.all().delete()

        for each in alphabet_list:
            new_name = 'Diner ' + each
            new_answer = Answer.objects.create(answer=new_name)

            total_info = len(info)
            random_number = randrange(2, 4)
            print(total_info, random_number)
            random_info = random.sample(info, random_number)
            print(random_info)
            for item in random_info:
                description = Description()
                description.answer = new_answer
                description.text_info = item
                description.digital_info = randrange(0, 100)
                description.save()
