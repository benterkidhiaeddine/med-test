import uuid
from django.db import models
from ..mixins.model_mixins import TimeStamps


class Answer(TimeStamps):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # the answers will be for example a list of ["abc", "bd"]
    letters_combinations = models.CharField(max_length=5)

    question = models.ForeignKey(
        "Question",
        on_delete=models.CASCADE,
        related_name="answers",
        related_query_name="answer",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.letters_combinations
