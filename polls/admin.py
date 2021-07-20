from django.contrib import admin
from .models import Question, VotesCounter, Description, Voter, Answer, Info


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
    list_display = ('question', 'answer', 'votes')


class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('answer', 'text_info', 'digital_info')


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(VotesCounter, VoteCounterAdmin)
admin.site.register(Description, DescriptionAdmin)
admin.site.register(Voter, VoterAdmin)
admin.site.register(Answer)
admin.site.register(Info)
