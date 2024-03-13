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
        "get_chapter",
        "get_subject",
        "get_medical_year",
    ]

    @admin.display(ordering="question_chapter", description="Chapter")
    def get_chapter(self, obj):
        return obj.course.chapter

    @admin.display(ordering="question_subject", description="Subject")
    def get_subject(self, obj):
        return obj.course.chapter.subject

    @admin.display(ordering="question_medical_year", description="Medical Year")
    def get_medical_year(self, obj):
        return obj.course.chapter.subject.medical_year

    # Pagination
    list_per_page = 10

    inlines = [ChoiceInLine, AnswerInLine]
