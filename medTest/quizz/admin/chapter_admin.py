from django.contrib import admin


class ChapterAdmin(admin.ModelAdmin):
    list_filter = ["subject", "subject__medical_year"]
    list_display = ["name", "subject", "get_medical_year"]

    search_fields = ["subject"]

    @admin.display(ordering="subject__medical_year", description="Medical_Year")
    def get_medical_year(self, obj):
        return obj.subject.medical_year

    pass
