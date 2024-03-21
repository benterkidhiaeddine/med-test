import uuid
from django.db import models
from ..mixins.model_mixins import TimeStamps

from .question import Question
from .clinical_case import ClinicalCase


class Chapter(TimeStamps):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(
        "Subject",
        on_delete=models.CASCADE,
        related_name="chapters",
        related_query_name="chapter",
        null=True,
        blank=True,
    )

    @property
    def theory_questions_count(self):
        return Question.objects.filter(
            course__chapter__id=self.id, is_clinical=False
        ).count()

    @property
    def clinical_cases_count(self):
        return ClinicalCase.objects.filter(course__chapter__id=self.id).count()

    def __str__(self) -> str:
        return self.name
