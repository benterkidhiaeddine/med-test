import json
import os

from django.conf import settings
from django.db import migrations





def load_subjects(apps, schema_editor):
    Subject = apps.get_model("quizz", "Subject")
    MedicalYear = apps.get_model("quizz", "MedicalYear")

    base_dir = settings.BASE_DIR
    json_file_path = os.path.join(base_dir,"quizz", "data" , "years_modules.json")



    with open(json_file_path) as f:
        years_modules = json.load(f)

    
    for year in years_modules.keys():
        medical_year = MedicalYear.objects.filter(label = year).first()
        for module in years_modules[year]:
            subject = Subject(name=module["name"], medical_year = medical_year)
            subject.save()

class Migration(migrations.Migration):
    dependencies = [
        ("quizz", "load_years"),
    ]

    operations = [
        migrations.RunPython(load_subjects),
    ]