from django.contrib import admin


class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name", "medical_year"]
    list_filter = ["medical_year", "created_at", "updated_at"]
    search_fields = ["name"]
    date_hierarchy = "created_at"
    ordering = ["created_at", "updated_at"]
