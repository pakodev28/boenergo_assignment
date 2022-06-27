from django.db import models

from .colorgenerator import get_three_color_string


class ColorObjects(models.Model):
    """Массив цветов, хранится в виде строки
    в которой цвета идут через запятую."""

    color_objects_string = models.TextField(
        verbose_name="Массив цветных объектов", default=get_three_color_string
    )

    class Meta:
        verbose_name = "Массив цветов"


class Answer(models.Model):
    guessed_index_number = models.PositiveSmallIntegerField(
        verbose_name="Угадываемый порядковый номер в массиве цветов"
    )
    guessed_answer = models.CharField(
        max_length=5, verbose_name="Отгаданный программой ответ"
    )
    is_correct = models.BooleanField(verbose_name="Правильность ответа")
    color_objects = models.ForeignKey(
        ColorObjects,
        on_delete=models.CASCADE,
        verbose_name="Массив цветных объектов",
    )

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
