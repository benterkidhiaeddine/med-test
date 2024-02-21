import uuid
import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

#Model mixins
class TimeStamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



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


class Subject(TimeStamps):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    medical_year = models.ForeignKey('MedicalYear', on_delete= models.CASCADE, 
        related_name="subjects",
        related_query_name="subject",
        null=True,
        blank=True
         )

    
    
    def __str__(self) -> str:
        return self.name

class Chapter(TimeStamps):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 100 )
    subject = models.ForeignKey('Subject' , on_delete = models.CASCADE,  
        related_name="chapters",
        related_query_name="chapter",null=True,
        blank=True
    )
    def __str__(self) -> str:
        return self.name

class Course(TimeStamps):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    chapter = models.ForeignKey( 'Chapter',
        on_delete=models.CASCADE,
        related_name="courses",
        related_query_name="course",null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.name


class ClinicalCase(TimeStamps):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    scenario = models.TextField()

    
    course = models.ForeignKey(
        'Course',
        on_delete=models.CASCADE,
        related_name="clinical_cases",
        related_query_name="clinical_case",
        blank= True,
        null=True
    )

    


class Question(TimeStamps):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField(null=True, blank =True)
    calender_year = models.IntegerField()
    content = models.TextField()
    course = models.ForeignKey(
        'Course',
        on_delete=models.CASCADE,
        related_name="questions",
        related_query_name="question",null=True,
        blank=True
    )
    clinical_case = models.ForeignKey(
        'ClinicalCase',
        on_delete=models.CASCADE,
        related_name="questions",
        related_query_name="question",null=True,
        blank=True
    )


    def __str__(self) -> str:
        return self.content[0:10]




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
        'Question',
        on_delete=models.CASCADE,
        related_name="choices",
        related_query_name="choice",
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.content



class Answer(TimeStamps):
   
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   
    #the answers will be for example a list of ["abc", "bd"] 
    letters_combinations = models.CharField(max_length = 5)

    question = models.ForeignKey(
        'Question',
        on_delete = models.CASCADE,
        related_name = 'answers',
        related_query_name = 'answer',  null=True,
        blank=True
    )