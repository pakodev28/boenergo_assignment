from django.contrib import admin

from .models import Answer, ColorObjects


class ColorObjectsAdmin(admin.ModelAdmin):
    list_display = ("pk", "color_objects_string")


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "guessed_index_number",
        "guessed_answer",
        "is_correct",
        "color_objects",
    )


admin.site.register(ColorObjects, ColorObjectsAdmin)
admin.site.register(Answer, AnswerAdmin)
