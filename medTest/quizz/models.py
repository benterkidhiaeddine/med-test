from django.db import models
from django.utils.translation import gettext_lazy as _

import datetime

# Create your models here.


class Subject(models.Model):
    # Medical years as choices

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="courses",
        related_query_name="course",
    )

    def __str__(self) -> str:
        return self.title


class Question(models.Model):
    # Choices question can of chapter Theory or Clinical Case
    class MedSchoolYear(models.IntegerChoices):
        FIRST_YEAR = 1, _("First year")
        SECOND_YEAR = 2, _("Second Year")
        THIRD_YEAR = 3, _("Third Year")
        FOURTH_YEAR = 4, _("Fourth Year")
        FIFTH_YEAR = 5, _("Sixth Year")
        SIXTH_YEAR = 6, _("Seventh Year")

    CALENDER_YEARS = [(y, y) for y in range(2000, datetime.datetime.now().year + 1)]

    med_school_year = models.IntegerField(choices=MedSchoolYear)  # type: ignore
    calender_year = models.IntegerField(choices=CALENDER_YEARS)
    content = models.TextField()
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="questions",
        related_query_name="question",
    )

    def __str__(self) -> str:
        top_str = self.content
        return top_str


class Choice(models.Model):
    # Letters Choices
    class Letter(models.TextChoices):
        A = "a", _("A")
        B = "b", _("B")
        C = "c", _("C")
        D = "d", _("D")
        E = "e", _("E")

    content = models.CharField(max_length=250)
    isCorrect = models.BooleanField()
    letter = models.CharField(max_length=1, choices=Letter)  # type: ignore
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="choices",
        related_query_name="choice",
    )

    def __str__(self) -> str:
        return self.content
