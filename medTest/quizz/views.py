from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from quizz.serializers.medical_school_year import MedicalSchoolYearSerializer
from quizz.serializers.subject import SubjectSerializer
from quizz.serializers.course import CourseSerializer

from quizz.models import MedicalYear, Subject, Chapter, Course


# Create your views here.


def home(request):
    return render(request, template_name="quizz/index.html")


# TODO View to return the years ids
@api_view(["GET"])
def medical_school_years(request):
    medical_years = MedicalYear.objects.all()
    serializer = MedicalSchoolYearSerializer(medical_years, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def subjects(request, medical_year_id):

    subjects = Subject.objects.filter(medical_year__id=medical_year_id)
    # Maybe change this error handling to a custom json?
    if len(subjects) == 0:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def chapters(request, subject_id):
    chapters = Chapter.objects.filter(subject__id=subject_id)
    # Maybe change this error handling to a custom json?
    if len(chapters) == 0:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SubjectSerializer(chapters, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def courses(request, chapter_id):
    courses = Course.objects.filter(chapter_id=chapter_id)
    # Maybe change this error handling to a custom json?
    if len(courses) == 0:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# TODO View to return the theoretical questions for each course
def clinical_cases(request):
    pass


# TODO View to return the clinical_cases for each course
def questions(request):
    pass
