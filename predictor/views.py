from django.shortcuts import render, redirect

from .models import Answer, ColorObjects
from .forms import AnswerForm
from .workers import try_to_guess_color


def new_color_objects_arr(request):
    """Вьющка создает Массив Цветов и редиректит на страницу угадывания."""
    if request.method == "POST":
        instance = ColorObjects()
        instance.save()
        return redirect("/predictor/guess_color/")
    return render(request, "predictor/create_color_arr.html", context={})


def guess_colore(request):
    """Вьюшка принемает порядковый номер объекта цвета и создает Ответ.
    Затем редиректит на страницу с результатом."""
    if request.method == "POST":
        color_objects = ColorObjects.objects.last()
        color_string_to_list = color_objects.color_objects_string.split(",")
        form = AnswerForm(request.POST)
        if form.is_valid():
            guessed_index_number = form.cleaned_data["guessed_index_number"]
            guessed_color = try_to_guess_color(
                color_string_to_list, guessed_index_number
            )
            answer = form.save(commit=False)
            answer.guessed_index_number = guessed_index_number
            answer.guessed_answer = guessed_color.get("guessed_color")
            answer.is_correct = guessed_color.get("is_correct")
            answer.color_objects = color_objects
            answer.save()
            return redirect("/predictor/is_the_color_guessed/")
    else:
        form = AnswerForm()
        context = {"form": form}
    return render(request, "predictor/guess_color.html", context=context)


def is_the_color_guessed(request):
    """Вьющка выводит результат вьюшки guess_colore."""
    answer = Answer.objects.last()
    color_arr = answer.color_objects.color_objects_string.split(",")
    right_color = color_arr[answer.guessed_index_number - 1]
    context = {"answer": answer, "right_color": right_color}
    return render(
        request, "predictor/is_the_color_guessed.html", context=context
    )
