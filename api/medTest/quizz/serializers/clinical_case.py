from rest_framework import serializers
from .question import QuestionResponseSerializer

from ..models.clinical_case import ClinicalCase


class ClinicalCaseResponseSerializer(serializers.ModelSerializer):
    questions = QuestionResponseSerializer(many=True)

    class Meta:
        model = ClinicalCase
        fields = ["id", "scenario", "questions"]
