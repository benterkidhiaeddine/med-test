import json
import os

from django.conf import settings
from django.db import migrations


def load_theory_questions(apps, schema_editor):
    Subject = apps.get_model("quizz", "Subject")
    Chapter = apps.get_model("quizz", "Chapter")
    Course = apps.get_model("quizz", "Course")
    Question = apps.get_model("quizz", "Question")
    Choice = apps.get_model("quizz", "Choice")
    Answer = apps.get_model("quizz", "Answer")

    base_dir = settings.BASE_DIR
    json_file_path = os.path.join(base_dir, "quizz", "data", "course_questions.json")

    # function that create clinicalCases
    def parse_question(question, course):

        choices = []
        answers = []
        # Create the choice instances in the db
        for choice in question["choices"]:
            created_choice = Choice.objects.create(
                content=choice["content"], letter=choice["letter"].lower()
            )
            choices.append(created_choice)
        # Create the question instances in the db
        for answer in question["answers"]:
            created_answer = Answer.objects.create(letters_combinations=answer)
            answers.append(created_answer)

        created_question = Question.objects.create(
            content=question["content"],
            calender_year=question["year"],
            is_clinical=False,
            course=course,
        )
        # Associate the choices and the answers with the question
        created_question.choices.add(*choices)
        created_question.answers.add(*answers)

    with open(json_file_path, encoding="utf-8") as f:
        course_questions = json.load(f)

    for module_year_chapter_course in course_questions.keys():
        # Split the key to get the medical year and subject name
        subject_name = module_year_chapter_course.split("_")[0]
        year_label = module_year_chapter_course.split("_")[1]
        chapter_name = module_year_chapter_course.split("_")[2]
        course_name = module_year_chapter_course.split("_")[3]

        course = Course.objects.filter(
            chapter__subject__medical_year__label=year_label,
            chapter__subject__name=subject_name,
            chapter__name=chapter_name,
            name=course_name,
        ).first()
        # Access the  theory questions in a specific course
        for theory_question in course_questions[module_year_chapter_course]:
            # Parse and save into db
            parse_question(theory_question, course)


class Migration(migrations.Migration):
    dependencies = [
        ("quizz", "load_clinicals"),
    ]

    operations = [
        migrations.RunPython(load_theory_questions),
    ]
