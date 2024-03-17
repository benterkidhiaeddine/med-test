from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from quizz.serializers.medical_school_year import MedicalSchoolYearSerializer
from quizz.serializers.subject import SubjectSerializer
from quizz.serializers.course import CourseSerializer
from quizz.serializers.available_years_payload import AvailableYearsPayloadSerializer
from quizz.serializers.available_years_response import AvailableYearsResponseSerializer

from quizz.models import MedicalYear, Subject, Chapter, Course, Question, ClinicalCase


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


# View to get the available years for the questions or the clinical cases according
# To the selected courses
@api_view(["POST"])
def available_years(request):
    serializer = AvailableYearsPayloadSerializer(data=request.data)
    if serializer.is_valid():
        payload = serializer.data
        course_id_list = payload["course_id_list"]

        available_years = set()

        for course_id in course_id_list:
            # Query the questions table to get the available distinct years there
            question_years = list(
                Question.objects.filter(course__id=course_id, is_clinical=False)
                .values("calender_year")
                .distinct()
            )
            # Query the clinical case table to get the available distinct years there
            clinical_cases_years = list(
                ClinicalCase.objects.filter(course__id=course_id)
                .values("calender_year")
                .distinct()
            )

            # Transform from the dict list to just a list containing the years
            question_years = [el["calender_year"] for el in question_years]
            clinical_cases_years = [el["calender_year"] for el in clinical_cases_years]

            available_years.update(question_years, clinical_cases_years)

        # Create a serializer to json encode the list of available years
        serializer = AvailableYearsResponseSerializer(
            data={"available_years": list(available_years)}
        )
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        # If somthing went wrong doing the processing return a status error
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(status=status.HTTP_400_BAD_REQUEST)


# TODO View to return the theoretical questions for each course
def clinical_cases(request):
    pass


# TODO View to return the clinical_cases for each course
def questions(request):
    pass
