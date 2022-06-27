from django.forms import ModelForm

from .models import QuadraticEquation


class QuadraticEquationForm(ModelForm):
    class Meta:
        model = QuadraticEquation
        fields = ["operand_a", "operand_b", "operand_c"]
        labels = {
            "operand_a": "введите a",
            "operand_b": "введите b",
            "operand_c": "введите c",
        }
