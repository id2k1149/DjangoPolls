from django.contrib import admin
from .models import Question, Answer, Description, Record, Diner


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


class RecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'question', 'answer')


class AnswerAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Description)
admin.site.register(Record, RecordAdmin)
admin.site.register(Diner)
