from rest_framework import serializers
from ..models.subject import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "name", "theory_questions_count", "clinical_cases_count"]
