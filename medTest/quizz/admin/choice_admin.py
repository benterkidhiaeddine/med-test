from django.contrib import admin


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["letter", "content"]
    search_fields = ["question__content"]
    pass
