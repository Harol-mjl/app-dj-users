from rest_framework import serializers
from apps.test_app.models.test import Test

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = [
            'id',
            'title',
            'description',
        ]
