from rest_framework import serializers

class TestField(serializers.Field):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)