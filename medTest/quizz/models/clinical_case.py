import uuid
from django.db import models
from ..mixins.model_mixins import TimeStamps


class ClinicalCase(TimeStamps):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    scenario = models.TextField()
    calender_year = models.IntegerField(null=True, blank=True)

    course = models.ForeignKey(
        "Course",
        on_delete=models.CASCADE,
        related_name="clinical_cases",
        related_query_name="clinical_case",
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.course.name} clinical case"
