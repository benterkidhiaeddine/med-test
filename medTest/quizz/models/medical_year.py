import uuid
from django.db import models

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

    def __str__(self) -> str:
        return self.label
