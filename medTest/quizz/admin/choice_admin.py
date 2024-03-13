from django.contrib import admin


class ChoiceAdmin(admin.ModelAdmin):

    search_fields = ["question__content"]
    pass
