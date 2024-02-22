from django.db import migrations


def load_years(apps, schema_editor):
    MedicalYear = apps.get_model("quizz", "MedicalYear")
    medical_years = ['1st', '2nd', '3rd', '4th', '5th', '6th', 'residency']
    for year in medical_years:
        medical_year = MedicalYear(label=year)
        medical_year.save()




class Migration(migrations.Migration):
    dependencies = [
        ("quizz", "0002_alter_clinicalcase_course"),
    ]

    operations = [
        migrations.RunPython(load_years),
    ]