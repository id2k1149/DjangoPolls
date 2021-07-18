from django.contrib import admin
from .models import Question, VotesCounter, Description, Voter, Answer


class VotesCounterInline(admin.TabularInline):
    model = VotesCounter
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
    inlines = [VotesCounterInline]

    list_display = ('title', 'date_published', 'result')


class VoterAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'question', 'answer')


class VoteCounterAdmin(admin.ModelAdmin):
    list_display = ('answer_id', 'votes')


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(VotesCounter, VoteCounterAdmin)
admin.site.register(Description)
admin.site.register(Voter, VoterAdmin)
admin.site.register(Answer)
