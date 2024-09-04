from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors136892ViewSet

router = DefaultRouter()
router.register(
    "testconnectors136892", Testconnectors136892ViewSet, basename="testconnectors136892"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
