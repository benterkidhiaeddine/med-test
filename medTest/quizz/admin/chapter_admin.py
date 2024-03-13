from django.contrib import admin


class ChapterAdmin(admin.ModelAdmin):
    list_filter = ["subject", "subject__medical_year"]
    pass
