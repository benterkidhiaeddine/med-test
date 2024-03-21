from rest_framework import serializers
from ..models.chapter import Chapter


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ["id", "name", "theory_question_count", "clinical_cases_count"]
