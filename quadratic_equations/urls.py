from django.urls import path

from . import views

urlpatterns = [
    path(
        "find_quadratic_equation_roots/",
        views.find_quadratic_equation_roots,
        name="find_quadratic_equation_roots",
    ),
    path(
        "result/<int:quadratic_equations_id>/",
        views.show_quadratic_equations_roots,
        name="show_quadratic_equations_roots",
    ),
]
