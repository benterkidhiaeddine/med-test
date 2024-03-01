import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from ..mixins.model_mixins import TimeStamps


class Choice(TimeStamps):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Letters Choices
    class Letter(models.TextChoices):
        A = "a", _("A")
        B = "b", _("B")
        C = "c", _("C")
        D = "d", _("D")
        E = "e", _("E")

    content = models.CharField(max_length=250)
    letter = models.CharField(max_length=1, choices=Letter)  # type: ignore
    question = models.ForeignKey(
        "Question",
        on_delete=models.CASCADE,
        related_name="choices",
        related_query_name="choice",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.content
