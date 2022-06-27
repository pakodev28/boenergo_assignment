from django.contrib import admin

from .models import QuadraticEquation


class QuadraticEquationAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "operand_a",
        "operand_b",
        "operand_c",
        "result",
    )


admin.site.register(QuadraticEquation, QuadraticEquationAdmin)
