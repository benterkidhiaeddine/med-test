import json
import os

from django.conf import settings
from django.db import migrations





def load_courses(apps, schema_editor):
    Subject = apps.get_model("quizz", "Subject")
    Chapter = apps.get_model("quizz", "Chapter")
    Course = apps.get_model("quizz", "Course")

    base_dir = settings.BASE_DIR
    json_file_path = os.path.join(base_dir,"quizz", "data" , "chapter_courses.json")



    with open(json_file_path) as f:
        chapter_courses = json.load(f)

   
    for module_year_chapter in chapter_courses.keys():
        #Split the key to get the medical year and subject name
        subject_name = module_year_chapter.split("_")[0]
        year_label = module_year_chapter.split("_")[1]
        chapter_name = module_year_chapter.split("_")[2]

        chapter = Chapter.objects.filter(subject__medical_year__label=year_label, subject__name = subject_name, name = chapter_name).first()
        #Access the chapters for the module in a specific year
        for course in chapter_courses[module_year_chapter]:
            course_obj = Course(name = course["name"] ,chapter = chapter)
            course_obj.save()
        
    
    
class Migration(migrations.Migration):
    dependencies = [
        ("quizz", "load_chapters"),
    ]

    operations = [
        migrations.RunPython(load_courses),
    ]