from django.contrib import admin
from ..models.question import Question
from ..models.clinical_case import ClinicalCase


class ClinicalCaseInLine(admin.TabularInline):
    model = ClinicalCase
    fields = ["id", "scenario"]
    readonly_fields = ["id", "scenario"]
    show_change_link = True


class QuestionInLine(admin.TabularInline):
    model = Question
    fields = ["id", "content"]
    readonly_fields = ["id", "content"]
    show_change_link = True


class CourseAdmin(admin.ModelAdmin):
    list_filter = ["chapter", "chapter__subject", "chapter__subject__medical_year"]
    list_display = ["name", "chapter", "get_chapter", "get_subject", "get_medical_year"]

    search_fields = ["id"]

    @admin.display(ordering="course_chapter", description="Chapter")
    def get_chapter(self, obj):
        return obj.chapter

    @admin.display(ordering="course_subject", description="Subject")
    def get_subject(self, obj):
        return obj.chapter.subject

    @admin.display(ordering="course_medical_year", description="Medical Year")
    def get_medical_year(self, obj):
        return obj.chapter.subject.medical_year

    inlines = [ClinicalCaseInLine, QuestionInLine]
