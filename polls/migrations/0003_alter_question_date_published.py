# Generated by Django 3.2.5 on 2021-07-15 23:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_question_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 15, 19, 11, 20, 828912)),
        ),
    ]