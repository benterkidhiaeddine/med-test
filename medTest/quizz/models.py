import uuid
import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class MedicalYear(models.Model):
    MEDICAL_YEARS = [
        ("1st" , "First year"),
        ("2nd" , "Second Year"),
        ("3rd" , "Third Year") ,
        ("4th" , "Fourth Year"),
        ("5th" , "Fifth Year") , 
        ("6th" , "Sixth Year") ,
        ("residency" , "Residency")
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length = 9,choices=MEDICAL_YEARS)

class Subject(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    medical_year = models.ForeignKey('MedicalYear', on_delete= models.CASCADE, 
        related_name="subjects",
        related_query_name="subject",
         )

    def __str__(self) -> str:
        return self.name

class Chapter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 100 )
    subject = models.ForeignKey('Subject' , on_delete = models.CASCADE,  
        related_name="chapters",
        related_query_name="chapter",
    )
    def __str__(self) -> str:
        return self.name

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    chapter = models.ForeignKey( 'Chapter',
        on_delete=models.CASCADE,
        related_name="courses",
        related_query_name="course",
    )

    def __str__(self) -> str:
        return self.name


class ClinicalCase(models.Model):

    scenario = models.TextField()

    
    course = models.ForeignKey(
        'Course',
        on_delete=models.CASCADE,
        related_name="clinical_cases",
        related_query_name="clinical_case",
    )

    


class Question(models.Model):

    number = models.IntegerField(null=True, blank =True)
    calender_year = models.IntegerField()
    content = models.TextField()
    course = models.ForeignKey(
        'Course',
        on_delete=models.CASCADE,
        related_name="questions",
        related_query_name="question",
    )
    clinical_case = models.ForeignKey(
        'ClinicalCase',
        on_delete=models.CASCADE,
        related_name="questions",
        related_query_name="question",
    )


    def __str__(self) -> str:
        return self.content[0:10]




class Choice(models.Model):
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
        'Question',
        on_delete=models.CASCADE,
        related_name="choices",
        related_query_name="choice",
    )

    def __str__(self) -> str:
        return self.content



class Answer(models.Model):
   
   
    #the answers will be for example a list of ["abc", "bd"] 
    letters_combinations = models.CharField(max_length = 5)

    question = models.ForeignKey(
        'Question',
        on_delete = models.CASCADE,
        related_name = 'answers',
        related_query_name = 'answer'
    )