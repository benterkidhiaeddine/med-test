import uuid
from django.db import models
from ..mixins.model_mixins import TimeStamps


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

    def __str__(self) -> str:
        return self.name
