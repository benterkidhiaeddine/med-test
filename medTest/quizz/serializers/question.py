from rest_framework import serializers
from .answer import AnswerSerializer
from .choice import ChoiceSerializer

from ..models.question import Question


class QuestionResponseSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ["id", "number", "content", "choices", "answers", "is_clinical"]
