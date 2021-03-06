# Generated by Django 3.2.9 on 2022-06-13 09:05

from django.db import migrations, models
import django.db.models.deletion
import predictor.colorgenerator


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ColorObjects",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "color_objects_string",
                    models.TextField(
                        default=predictor.colorgenerator.get_three_color_string,
                        verbose_name="Массив цветных объектов",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Answer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "guessed_index_number",
                    models.PositiveSmallIntegerField(
                        verbose_name="Угадываемый порядковый номер в массиве цветов"
                    ),
                ),
                (
                    "guessed_answer",
                    models.CharField(
                        max_length=5,
                        verbose_name="Отгаданный программой ответ",
                    ),
                ),
                (
                    "is_correct",
                    models.BooleanField(verbose_name="Правильность ответа"),
                ),
                (
                    "color_objects",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="predictor.colorobjects",
                        verbose_name="Массив цветных объектов",
                    ),
                ),
            ],
        ),
    ]
