import uuid

from django.db import models
from ..mixins.model_mixins import TimeStamps


class Subject(TimeStamps):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    medical_year = models.ForeignKey(
        "MedicalYear",
        on_delete=models.CASCADE,
        related_name="subjects",
        related_query_name="subject",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name
