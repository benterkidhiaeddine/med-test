from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from quizz.serializers.medical_school_year import MedicalSchoolYearSerialize
from quizz.models import MedicalYear

# Create your views here.


def home(request):
    return render(request, template_name="quizz/index.html")


# TODO View to return the years ids
@api_view(["GET"])
def medical_school_years(request):
    medical_years = MedicalYear.objects.all()
    serializer = MedicalSchoolYearSerialize(medical_years, many=True)
    return Response(serializer.data)


# TODO View to return the subjects for each year
def subjects(request):
    pass


# TODO View to return the chapters for each subject
def chapters(request):
    pass


# TODO View to return the courses for each chapter
def courses(request):
    pass


# TODO View to return the theoretical questions for each course
def courses(request):
    pass


# TODO View to return the clinical_case questions for each course
def courses(request):
    pass
