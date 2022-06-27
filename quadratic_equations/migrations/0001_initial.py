# Generated by Django 3.2.9 on 2022-06-27 02:05

from django.db import migrations, models
import quadratic_equations.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="QuadraticEquation",
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
                    "operand_a",
                    models.IntegerField(
                        validators=[
                            quadratic_equations.models.validate_not_zero
                        ],
                        verbose_name="Значение 'a'",
                    ),
                ),
                (
                    "operand_b",
                    models.IntegerField(verbose_name="Значение 'b'"),
                ),
                (
                    "operand_c",
                    models.IntegerField(verbose_name="Значение 'c'"),
                ),
                (
                    "result",
                    models.CharField(max_length=50, verbose_name="Результат"),
                ),
            ],
        ),
    ]
