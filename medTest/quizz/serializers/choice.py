from rest_framework import serializers
from ..models.choice import Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["letter", "content"]
