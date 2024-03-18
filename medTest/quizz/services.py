from typing import List
from uuid import UUID


from .models.question import Question
from .models.clinical_case import ClinicalCase


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
