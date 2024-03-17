from rest_framework import serializers


# This is just a list field with a child UUID field to accept a list
# of subject ids
class UUIDListField(serializers.ListField):
    child = serializers.UUIDField()
