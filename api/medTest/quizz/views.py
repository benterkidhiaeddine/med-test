from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from quizz.serializers.medical_school_year import MedicalSchoolYearSerializer
from quizz.serializers.subject import SubjectSerializer
from quizz.serializers.course import CourseSerializer
from quizz.serializers.available_years_payload import AvailableYearsPayloadSerializer
from quizz.serializers.available_years_response import AvailableYearsResponseSerializer
from quizz.serializers.revision_payload import RevisionPayload
from quizz.serializers.question import QuestionResponseSerializer
from quizz.serializers.clinical_case import ClinicalCaseResponseSerializer

from quizz.services import (
    get_available_years,
    get_revision_items,
    get_medical_years,
    get_subjects_by_medical_year_id,
    get_chapters_by_subject_id,
    get_courses_by_chapter_id,
)

from quizz.models import MedicalYear, Subject, Chapter, Course, Question, ClinicalCase


# Create your views here.


def home(request):
    return render(request, template_name="quizz/index.html")


@api_view(["GET"])
def medical_school_years(request):
    response_data = get_medical_years()
    return Response(response_data)


@api_view(["GET"])
def subjects(request, medical_year_id):
    # This is important if client tries to access a medical year that dosen't exist
    medical_year = get_object_or_404(MedicalYear, id=medical_year_id)

    response_data = get_subjects_by_medical_year_id(medical_year_id)
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(["GET"])
def chapters(request, subject_id):

    subject = get_object_or_404(Subject, id=subject_id)
    response_data = get_chapters_by_subject_id(subject_id)

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(["GET"])
def courses(request, chapter_id):

    chapter = get_object_or_404(Chapter, id=chapter_id)
    response_data = get_courses_by_chapter_id(chapter_id)
    return Response(response_data, status=status.HTTP_200_OK)


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


@api_view(["GET"])
def question_by_id(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    serializer = QuestionResponseSerializer(instance=question)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def clinical_case_by_id(request, clinical_case_id):

    clinical_case = get_object_or_404(ClinicalCase, pk=clinical_case_id)

    serializer = ClinicalCaseResponseSerializer(instance=clinical_case)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
