import uuid
from django.db import models

from .question import Question
from .clinical_case import ClinicalCase

# Create your models here.


class MedicalYear(models.Model):
    MEDICAL_YEARS = [
        ("1st", "First year"),
        ("2nd", "Second Year"),
        ("3rd", "Third Year"),
        ("4th", "Fourth Year"),
        ("5th", "Fifth Year"),
        ("6th", "Sixth Year"),
        ("residency", "Residency"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=9, choices=MEDICAL_YEARS)

    @property
    def theory_questions_count(self):
        return Question.objects.filter(
            course__chapter__subject__medical_year__id=self.id, is_clinical=False
        ).count()

    @property
    def clinical_cases_count(self):
        return ClinicalCase.objects.filter(
            course__chapter__subject__medical_year__id=self.id
        ).count()

    def __str__(self) -> str:
        return self.label
