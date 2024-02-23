from django.contrib import admin
from .models import (
    MedicalYear,
    Subject,
    Chapter,
    Course,
    Question,
    ClinicalCase,
    Choice,
    Answer,
)


@admin.register(MedicalYear)
class MedicalYearAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "medical_year"]
    list_filter = ["medical_year", "created_at", "updated_at"]
    search_fields = ["name"]
    date_hierarchy = "created_at"
    ordering = ["created_at", "updated_at"]
    pass


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(ClinicalCase)
class ClinicalCaseAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
