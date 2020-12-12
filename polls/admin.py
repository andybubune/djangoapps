from django.db import models
from django.contrib import admin
from .models import Choice, Question
# Create your models here.
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ]
    inlines = [ChoiceInline]
admin.site.register(Question, QuestionAdmin)
