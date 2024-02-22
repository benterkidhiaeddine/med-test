import json
import os

from django.conf import settings
from django.db import migrations





def load_clinicals(apps, schema_editor):
    Subject = apps.get_model("quizz", "Subject")
    Chapter = apps.get_model("quizz", "Chapter")
    Course = apps.get_model("quizz", "Course")
    ClinicalCase = apps.get_model("quizz", "ClinicalCase")
    Question = apps.get_model("quizz", "Question")
    Choice = apps.get_model("quizz", "Choice")
    Answer = apps.get_model("quizz", "Answer")

    base_dir = settings.BASE_DIR
    json_file_path = os.path.join(base_dir,"quizz", "data" , "course_clinicals.json")


    
    # function that create clinicalCases
    def parse_clinical(clinical, course):
        questions = [] 
        
        for question in clinical["questions"]:

            choices = []
            answers = []
            #Create the choice instances in the db
            for choice in question["choices"]:
                created_choice = Choice.objects.create(content=choice["content"] , letter=choice["letter"])
                choices.append(created_choice) 
            #Create the question instances in the db
            for answer in question["answers"]:
                created_answer = Answer.objects.create(letters_combinations=answer)
                answers.append(created_answer)

            created_question = Question.objects.create(content=question["content"] , number=question["number"], calender_year = clinical["year"], is_clinical=True, course = course) 
            #Associate the choices and the answers with the question
            created_question.choices.add(*choices)
            created_question.answers.add(*answers)
       
            questions.append(created_question) 

        created_clinical = ClinicalCase.objects.create(scenario=clinical["scenario"] , calender_year=clinical["year"], course = course )

        #associate the questions with the clinical case
        created_clinical.questions.add(*questions)

        return created_clinical
    
    

    with open(json_file_path) as f:
        course_clinicals = json.load(f)

   
    for module_year_chapter_course in course_clinicals.keys():
        #Split the key to get the medical year and subject name
        subject_name = module_year_chapter_course.split("_")[0]
        year_label = module_year_chapter_course.split("_")[1]
        chapter_name = module_year_chapter_course.split("_")[2]
        course_name = module_year_chapter_course.split("_")[3]

        course = Course.objects.filter(chapter__subject__medical_year__label=year_label, chapter__subject__name = subject_name, chapter__name = chapter_name, name = course_name).first()
        #Access the  clinicals in a specific course
        for clinical in course_clinicals[module_year_chapter_course]:
            #Parse and save into db
            clinical_obj = parse_clinical(clinical, course)
    
    
class Migration(migrations.Migration):
    dependencies = [
        ("quizz", "load_courses"),
    ]

    operations = [
        migrations.RunPython(load_clinicals),
    ]