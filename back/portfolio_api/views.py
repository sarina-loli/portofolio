from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from .filters import ProjectFilter, SkillFilter
from .models import ContactMessage, Education, Experience, Profile, Project, Service, Skill
from .permissions import IsAdminOrReadOnly
from .serializers import (
    ContactMessageSerializer,
    EducationSerializer,
    ExperienceSerializer,
    ProfileSerializer,
    ProjectDetailSerializer,
    ProjectListSerializer,
    ServiceSerializer,
    SkillSerializer,
)


class ProfileViewSet(viewsets.ModelViewSet):
    """Exposes the single Profile record.

    GET /api/profile/        -> list (returns the single profile as one object)
    GET /api/profile/<id>/    -> retrieve
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminOrReadOnly]

    def list(self, request, *args, **kwargs):
        profile = self.get_queryset().first()
        if not profile:
            return Response({})
        serializer = self.get_serializer(profile)
        return Response(serializer.data)


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_class = SkillFilter
    search_fields = ["name"]
    ordering_fields = ["order", "name", "proficiency"]
    pagination_class = None


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.prefetch_related("technologies__technology", "gallery").all()
    permission_classes = [IsAdminOrReadOnly]
    filterset_class = ProjectFilter
    search_fields = ["title", "summary", "description"]
    ordering_fields = ["order", "created_at", "title"]
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListSerializer
        return ProjectDetailSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = None
    ordering_fields = ["order", "start_date"]


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = None
    ordering_fields = ["order", "start_date"]


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = None
    ordering_fields = ["order"]


class ContactThrottle(AnonRateThrottle):
    scope = "contact"


class ContactMessageViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Public endpoint: anyone can POST a message. Nobody can read/list/update
    via the public API — messages are only viewable in Django admin, which
    keeps visitor-submitted personal data from being exposed on the API.
    """

    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    throttle_classes = [ContactThrottle]

    def get_permissions(self):
        # Anyone may create (submit) a message; nothing else is exposed
        # because only CreateModelMixin is wired up on this viewset.
        return []
