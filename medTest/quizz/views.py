from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from quizz.serializers.medical_school_year import MedicalSchoolYearSerializer
from quizz.serializers.subject import SubjectSerializer
from quizz.serializers.course import CourseSerializer
from quizz.serializers.available_years_payload import AvailableYearsPayloadSerializer
from quizz.serializers.available_years_response import AvailableYearsResponseSerializer
from quizz.serializers.revision_payload import RevisionPayload

from quizz.services import get_available_years, get_revision_items


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

        available_years = get_available_years(course_id_list)

        # Create a serializer to json encode the list of available years
        serializer = AvailableYearsResponseSerializer(
            data={"available_years": available_years}
        )
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        # If something went wrong doing the processing return a status error
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(status=status.HTTP_400_BAD_REQUEST)


# for the current selection of courses and calender years ,
# return a list of all available theoretical questions and clinical_cases objects
@api_view(["POST"])
def revision(request):
    serializer = RevisionPayload(data=request.data)

    if serializer.is_valid():
        payload = serializer.data
        course_id_list = payload["course_id_list"]
        source_years = payload["source_years"]

        revision_items = get_revision_items(course_id_list, source_years)

        return Response(data=revision_items, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


# TODO : Return a question object with all it's choices answer , source medical year, calender_year , chapter and course
