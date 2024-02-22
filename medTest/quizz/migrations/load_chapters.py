import json
import os

from django.conf import settings
from django.db import migrations





def load_chapters(apps, schema_editor):
    Subject = apps.get_model("quizz", "Subject")
    Chapter = apps.get_model("quizz", "Chapter")
     

    base_dir = settings.BASE_DIR
    json_file_path = os.path.join(base_dir,"quizz", "data" , "module_chapters.json")



    with open(json_file_path) as f:
        chapter_modules = json.load(f)

   
    for module_year in chapter_modules.keys():
        #Split the key to get the medical year and subject name
        subject_name = module_year.split("_")[0]
        year_label = module_year.split("_")[1]

        subject = Subject.objects.filter(medical_year__label=year_label, name = subject_name).first()
        #Access the chapters for the module in a specific year
        for chapter in chapter_modules[module_year]:
            chapter_obj = Chapter(name = chapter["name"] ,subject = subject)
            chapter_obj.save()
        
    
    
class Migration(migrations.Migration):
    dependencies = [
        ("quizz", "load_modules"),
    ]

    operations = [
        migrations.RunPython(load_chapters),
    ]