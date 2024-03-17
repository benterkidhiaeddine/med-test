from django.urls import path
from quizz import views
import uuid

urlpatterns = [
    path("", views.home),
    path("medical_years/", views.medical_school_years),
    path("medical_years/<uuid:medical_year_id>/subjects/", views.subjects),
    path("subjects/<uuid:subject_id>/chapters/", views.chapters),
    path("chapters/<uuid:chapter_id>/courses/", views.courses),
    path("available_years/", views.available_years),
    path("revision/", views.revision),
]
