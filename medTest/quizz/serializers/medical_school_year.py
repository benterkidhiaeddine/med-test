from rest_framework import serializers
from quizz.models import MedicalYear


class MedicalSchoolYearSerialize(serializers.ModelSerializer):
    class Meta:
        model = MedicalYear
        fields = ["id", "label"]
