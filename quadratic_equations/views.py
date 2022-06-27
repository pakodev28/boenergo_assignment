from math import sqrt

from django.shortcuts import render, redirect, get_object_or_404

from .forms import QuadraticEquationForm
from .models import QuadraticEquation


def find_quadratic_equation_roots(request):
    """Вьюшка вычисляет корни квадратного уравнения и создает запись в БД"""
    if request.method == "POST":
        form = QuadraticEquationForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data["operand_a"]
            b = form.cleaned_data["operand_b"]
            c = form.cleaned_data["operand_c"]
            discri = b * b - 4 * a * c
            if discri > 0:
                root_1 = (-b + sqrt(discri)) / (2 * a)
                root_2 = (-b - sqrt(discri)) / (2 * a)
                result = f"Корни: {root_1}, {root_2}"
            elif discri == 0:
                root = -b / (2 * a)
                result = f"Корень - {root}"
            else:
                result = "Так как дискриминант меньше нуля, то уравнение не имеет действительных решений"
            quadratic_equation = form.save(commit=False)
            quadratic_equation.result = result
            quadratic_equation.save()
            return redirect(
                f"/quadratic_equations/result/{quadratic_equation.id}/"
            )
    else:
        form = QuadraticEquationForm()
        context = {"form": form}
    return render(
        request,
        "quadratic_equations/quadratic_equations.html",
        context=context,
    )


def show_quadratic_equations_roots(request, quadratic_equations_id):
    """Вьюшка показывает результаты решения квадратного уравнения"""
    quadratic_equation = get_object_or_404(
        QuadraticEquation, id=quadratic_equations_id
    )
    context = {"quadratic_equation": quadratic_equation}
    return render(
        request,
        "quadratic_equations/quadratic_equations_result.html",
        context=context,
    )
