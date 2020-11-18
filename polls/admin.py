from django.contrib import admin
from .models import Choice, Question

# Register your models here.

from polls.models import Question


class QuestionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
