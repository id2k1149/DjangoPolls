# Generated by Django 3.2.5 on 2021-07-16 16:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0, verbose_name='Votes')),
            ],
        ),
        migrations.CreateModel(
            name='Diner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Where to have a lunch?', max_length=128, verbose_name='Question')),
                ('date_published', models.DateField(default=datetime.date.today)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active poll')),
                ('answers', models.ManyToManyField(to='polls.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.answer', verbose_name='Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question', verbose_name='Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=64)),
                ('digital_info', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('diner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.diner')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='diner_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.diner'),
        ),
    ]
