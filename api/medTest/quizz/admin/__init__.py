from quizz.admin.answer_admin import AnswerAdmin
from quizz.admin.medical_year_admin import MedicalYearAdmin
from quizz.admin.subject_admin import SubjectAdmin
from quizz.admin.chapter_admin import ChapterAdmin
from quizz.admin.clinical_case_admin import ClinicalCaseAdmin
from quizz.admin.course_admin import CourseAdmin
from quizz.admin.question_admin import QuestionAdmin
from quizz.admin.choice_admin import ChoiceAdmin

from quizz.models.medical_year import MedicalYear
from quizz.models.subject import Subject
from quizz.models.chapter import Chapter
from quizz.models.course import Course
from quizz.models.clinical_case import ClinicalCase
from quizz.models.question import Question
from quizz.models.choice import Choice
from quizz.models.answer import Answer


from django.contrib import admin

admin.site.register(MedicalYear, MedicalYearAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(ClinicalCase, ClinicalCaseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
