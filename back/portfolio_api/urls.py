from rest_framework.routers import DefaultRouter

from .views import (
    ContactMessageViewSet,
    EducationViewSet,
    ExperienceViewSet,
    ProfileViewSet,
    ProjectViewSet,
    ServiceViewSet,
    SkillViewSet,
)

router = DefaultRouter()
router.register("profile", ProfileViewSet, basename="profile")
router.register("skills", SkillViewSet, basename="skill")
router.register("projects", ProjectViewSet, basename="project")
router.register("experience", ExperienceViewSet, basename="experience")
router.register("education", EducationViewSet, basename="education")
router.register("services", ServiceViewSet, basename="service")
router.register("contact", ContactMessageViewSet, basename="contact")

urlpatterns = router.urls
