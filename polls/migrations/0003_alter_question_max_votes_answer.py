# Generated by Django 3.2.5 on 2021-07-16 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_max_votes_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='max_votes_answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.diner', verbose_name='Result'),
        ),
    ]