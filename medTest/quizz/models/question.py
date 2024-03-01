import uuid
from django.db import models
from ..mixins.model_mixins import TimeStamps


class Question(TimeStamps):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField(null=True, blank=True)
    calender_year = models.IntegerField()
    content = models.TextField()
    is_clinical = models.BooleanField(null=True, blank=True)

    course = models.ForeignKey(
        "Course",
        on_delete=models.CASCADE,
        related_name="questions",
        related_query_name="question",
        null=True,
        blank=True,
    )
    clinical_case = models.ForeignKey(
        "ClinicalCase",
        on_delete=models.CASCADE,
        related_name="questions",
        related_query_name="question",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.content[0:20]
