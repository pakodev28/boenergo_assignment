from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("predictor/", include("predictor.urls")),
    path("quadratic_equations/", include("quadratic_equations.urls"))
]
