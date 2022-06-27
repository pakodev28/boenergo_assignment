from django.urls import path

from . import views

urlpatterns = [
    path(
        "create_colors/",
        views.new_color_objects_arr,
        name="new_color_objects_arr",
    ),
    path("guess_color/", views.guess_colore, name="guess_colore"),
    path(
        "is_the_color_guessed/",
        views.is_the_color_guessed,
        name="is_the_color_guessed",
    ),
]
