from rest_framework.routers import DefaultRouter
from apps.test_app.v1.views import TestViewSet

router = DefaultRouter()
router.register(r'test', TestViewSet, basename='test')
urlpatterns = router.urls