from django.contrib import admin
from ..models.choice import Choice
from ..models.answer import Answer


class ChoiceInLine(admin.TabularInline):
    model = Choice
    fields = ["letter", "content"]
    readonly_fields = ["letter", "content"]
    ordering = ["letter"]


class AnswerInLine(admin.TabularInline):
    model = Answer
    fields = ["letters_combinations"]
    readonly_fields = ["letters_combinations"]
    ordering = ["letters_combinations"]


class QuestionAdmin(admin.ModelAdmin):

    list_filter = [
        "calender_year",
        "is_clinical",
        "course",
        "course__chapter",
        "course__chapter__subject",
    ]
    list_display = [
        "content",
        "calender_year",
        "is_clinical",
        "course",
    ]

    inlines = [ChoiceInLine, AnswerInLine]
