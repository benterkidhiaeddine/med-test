from django.contrib import admin


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
    pass
