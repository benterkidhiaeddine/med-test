from django.contrib import admin


class AnswerAdmin(admin.ModelAdmin):
    fields = ["letters_combinations"]
    pass
