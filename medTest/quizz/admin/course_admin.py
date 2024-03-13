from django.contrib import admin


class CourseAdmin(admin.ModelAdmin):
    list_filter = ["chapter", "chapter__subject", "chapter__subject__medical_year"]
    pass
