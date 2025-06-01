from rest_framework import serializers
from .custom_serializer_fields import UUIDListField


# This is a custom serializer for the payload to specify the courses to look through to get
# the available calender years of the questions or the clinical cases
class AvailableYearsPayloadSerializer(serializers.Serializer):
    course_id_list = UUIDListField()
