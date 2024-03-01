import uuid

from django.db import models
from ..mixins.model_mixins import TimeStamps


class Course(TimeStamps):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    chapter = models.ForeignKey(
        "Chapter",
        on_delete=models.CASCADE,
        related_name="courses",
        related_query_name="course",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name
