from django.contrib import admin
from ..models.question import Question


class QuestionInLine(admin.TabularInline):
    model = Question
    fields = ["content"]
    readonly_fields = ["content"]
    ordering = ["number"]
    extra = 0


class ClinicalCaseAdmin(admin.ModelAdmin):
    list_filter = [
        "calender_year",
        "course",
        "course__chapter__subject",
        "course__chapter__subject__medical_year",
    ]
    list_display = [
        "scenario",
        "calender_year",
        "get_course",
        "get_chapter",
        "get_subject",
        "get_medical_year",
    ]

    inlines = [QuestionInLine]

    @admin.display(ordering="clinical_case_course", description="Course")
    def get_course(self, obj):
        return obj.course

    @admin.display(ordering="clinical_case_chapter", description="Chapter")
    def get_chapter(self, obj):
        return obj.course.chapter

    @admin.display(ordering="clinical_case_subject", description="Subject")
    def get_subject(self, obj):
        return obj.course.chapter.subject

    @admin.display(ordering="clinical_case_medical_year", description="Medical Year")
    def get_medical_year(self, obj):
        return obj.course.chapter.subject.medical_year

    pass
