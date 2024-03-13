from django.contrib import admin
from ..models.subject import Subject


class SubjectInLine(admin.TabularInline):
    model = Subject
    fields = ["name"]
    readonly_fields = ["name"]


class MedicalYearAdmin(admin.ModelAdmin):
    inlines = [SubjectInLine]
    ordering = ["label"]
    pass
