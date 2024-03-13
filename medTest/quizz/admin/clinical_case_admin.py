from django.contrib import admin


class ClinicalCaseAdmin(admin.ModelAdmin):
    list_filter = [
        "calender_year",
        "course",
        "course__chapter",
        "course__chapter__subject",
        "course__chapter__subject__medical_year",
    ]
    pass
