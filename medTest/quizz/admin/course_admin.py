from django.contrib import admin


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

    pass
