from django.urls import path
from quizz import views


urlpatterns = [path("", views.home), path("medical_years/", views.medical_school_years)]
