from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects.views import (ProfileViewSet,
                            ProjectViewSet,
                            CertificateViewSet,
                            CertifyingInstitutionViewSet)


router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"certificates", CertificateViewSet)
router.register(r"certifying-institutions", CertifyingInstitutionViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
