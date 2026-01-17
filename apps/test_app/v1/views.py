from rest_framework import viewsets
from apps.test_app.models.test import Test
from apps.test_app.v1.serializers import TestSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer