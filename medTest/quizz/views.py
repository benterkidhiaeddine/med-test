from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from quizz.serializers.medical_school_year import MedicalSchoolYearSerializer
from quizz.serializers.subject import SubjectSerializer

from quizz.models import MedicalYear, Subject


# Create your views here.


def home(request):
    return render(request, template_name="quizz/index.html")


# TODO View to return the years ids
@api_view(["GET"])
def medical_school_years(request):
    medical_years = MedicalYear.objects.all()
    serializer = MedicalSchoolYearSerializer(medical_years, many=True)
    return Response(serializer.data)


# TODO View to return the subjects for each year
@api_view(["GET"])
def subjects(request, medical_year_id):
    print(medical_year_id)
    subjects = Subject.objects.filter(medical_year__id=medical_year_id)
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


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
