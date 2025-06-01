from typing import List
from uuid import UUID


from .serializers.medical_school_year import MedicalSchoolYearSerializer
from .serializers.subject import SubjectSerializer
from .serializers.chapter import ChapterSerializer
from .serializers.course import CourseSerializer

from .models.medical_year import MedicalYear
from .models.question import Question
from .models.clinical_case import ClinicalCase
from .models.subject import Subject
from .models.chapter import Chapter
from .models.course import Course


def get_available_years(course_id_list: List[UUID]) -> List[int]:
    """
    This function return a list of available years from the question and clinical case tables using the
    the list of course ids

    Args:
        course_id_list (List[UUID]): The list of course ids , for which we want to get the available calender years that can be selected
        for the contained questions in said courses

    Returns:
        List[int] : List of available years
    """
    # I am using a set here to avoid collisions between years of theoretical questions and clinical cases calender years
    # But maybe this wouldn't be the case , because the selected courses will have either clinical cases or theory questions
    available_years = set()

    # Query the questions table to get the available distinct years there
    question_years = list(
        Question.objects.filter(course__id__in=course_id_list, is_clinical=False)
        .values("calender_year")
        .distinct()
    )

    # Query the clinical case table to get the available distinct years there
    clinical_cases_years = list(
        ClinicalCase.objects.filter(course__id__in=course_id_list)
        .values("calender_year")
        .distinct()
    )

    # Transform from the dict list to just a list containing the years
    question_years = [el["calender_year"] for el in question_years]
    clinical_cases_years = [el["calender_year"] for el in clinical_cases_years]

    available_years.update(question_years, clinical_cases_years)

    return list(available_years)


def get_revision_items(
    course_id_list: List[UUID], source_years: List[int]
) -> List[dict]:
    """

    this function returns a list of entities . an Entity in this context is a dict that contains information about
    the type of the entity : it's either a clinical case or a theory question plus it's corresponding id

    Args:
        course_id_list (List[UUID]): List of the course ids
        source_years (List[int]): List of the source years for which we want to filter the questions or the
        clinical cases

    Returns:
        List[dict]: it has the following shape
        [
            {
                "entity" : "clinical_case/theory_question",
                "id" : "UUID-example"
            },
            ...
        ]
    """
    # The list that will contain the queried ids and their entity type weather it's a clinical case or theoretical question
    items = []

    question_ids = Question.objects.filter(
        course__id__in=course_id_list,
        is_clinical=False,
        calender_year__in=source_years,
    ).values("id")

    question_items = [
        {"entity": "theory_question", "id": el["id"]} for el in question_ids
    ]
    items.extend(question_items)

    clinical_case_ids = ClinicalCase.objects.filter(
        course__id__in=course_id_list, calender_year__in=source_years
    ).values("id")

    clinical_case_items = [
        {"entity": "clinical_case", "id": el["id"]} for el in clinical_case_ids
    ]

    items.extend(clinical_case_items)

    return items


def get_medical_years():
    """
    returns  a list of medical years objects each containing the following information:
    - medical_year_id
    - medical_year_label or name
    - medical_year theoretical_question_count and clinical_cases count

    Returns:
        dict : dict object containing the list of medical years objects
    """
    medical_years = MedicalYear.objects.all()
    serializer = MedicalSchoolYearSerializer(medical_years, many=True)
    response_data = {"medical_years": serializer.data}

    return response_data


# TODO: document this function
def get_subjects_by_medical_year_id(medical_year_id: UUID) -> dict:

    subjects = Subject.objects.filter(medical_year__id=medical_year_id)
    serializer = SubjectSerializer(subjects, many=True)
    response_data = {"subjects": serializer.data}

    return response_data


def get_chapters_by_subject_id(subject_id: UUID) -> dict:
    chapters = Chapter.objects.filter(subject__id=subject_id)
    serializer = ChapterSerializer(chapters, many=True)
    response_data = {"chapters": serializer.data}

    return response_data


def get_courses_by_chapter_id(chapter_id: UUID) -> dict:
    courses = Course.objects.filter(chapter_id=chapter_id)
    serializer = CourseSerializer(courses, many=True)
    response_data = {"courses": serializer.data}
    return response_data
