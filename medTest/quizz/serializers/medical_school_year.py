from rest_framework import serializers
from ..models.medical_year import MedicalYear


class MedicalSchoolYearSerialize(serializers.ModelSerializer):
    class Meta:
        model = MedicalYear
        fields = ["id", "label"]
