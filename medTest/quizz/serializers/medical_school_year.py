from rest_framework import serializers
from ..models.medical_year import MedicalYear


class MedicalSchoolYearSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicalYear
        fields = ["id", "label", "theory_questions_count", "clinical_cases_count"]
