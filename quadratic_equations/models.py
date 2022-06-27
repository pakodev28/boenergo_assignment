from django.db import models
from django.core.exceptions import ValidationError


def validate_not_zero(value):
    if value == 0:
        raise ValidationError("'a' не может равняться нулю.")


class QuadraticEquation(models.Model):
    operand_a = models.IntegerField(
        verbose_name="Значение 'a'", validators=[validate_not_zero]
    )
    operand_b = models.IntegerField(verbose_name="Значение 'b'")
    operand_c = models.IntegerField(verbose_name="Значение 'c'")
    result = models.TextField(verbose_name="Результат")
