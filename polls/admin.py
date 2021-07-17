from django.contrib import admin
from .models import Question, VoteCounter, Description, Voter, Answer


class AnswerInline(admin.TabularInline):
    model = Question.answers.through
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['title', 'result']}
         ),
        ('Date info',
         {'fields': ['date_published'],
          'classes': ['collapse']}
         ),
    ]
    inlines = [AnswerInline]

    list_display = ('title', 'date_published', 'result')


class VoterAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'question', 'answer')


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(VoteCounter)
admin.site.register(Description)
admin.site.register(Voter, VoterAdmin)
admin.site.register(Answer)
