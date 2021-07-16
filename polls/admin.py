from django.contrib import admin
from .models import Question, Answer, Description, Record


# class AnswerInline(admin.TabularInline):
#     model = Answer
#     extra = 2
#
#
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,
#          {'fields': ['title', 'is_active']}
#          ),
#         ('Date info',
#          {'fields': ['date_published'],
#           'classes': ['collapse']}
#          ),
#     ]
#     inlines = [AnswerInline]
#
#     list_display = ('title', 'date_published', 'is_active')


class RecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'question', 'answer')


# Register your models here.
# admin.site.register(Question, QuestionAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Description)
admin.site.register(Record, RecordAdmin)
