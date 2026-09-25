from rest_framework import serializers

from .models import (
    ContactMessage,
    Education,
    Experience,
    Profile,
    Project,
    ProjectImage,
    Service,
    Skill,
    Technology,
)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "id",
            "full_name",
            "title",
            "tagline",
            "intro",
            "about",
            "philosophy",
            "specialties",
            "career_goals",
            "location",
            "email",
            "phone",
            "avatar",
            "resume",
            "github_url",
            "linkedin_url",
            "twitter_url",
            "tiktok_url",
            "website_url",
            "years_experience",
        ]


class SkillSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source="get_category_display", read_only=True)

    class Meta:
        model = Skill
        fields = ["id", "name", "category", "category_display", "icon", "proficiency", "order"]


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ["id", "name", "icon"]


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ["id", "image", "caption", "order"]


class ProjectListSerializer(serializers.ModelSerializer):
    """Lightweight serializer used for the project showcase / cards."""

    technologies = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "slug",
            "summary",
            "image",
            "github_url",
            "live_url",
            "case_study_url",
            "featured",
            "technologies",
        ]

    def get_technologies(self, obj):
        return TechnologySerializer(
            [pt.technology for pt in obj.technologies.select_related("technology")], many=True
        ).data


class ProjectDetailSerializer(serializers.ModelSerializer):
    """Full serializer for the project detail page."""

    technologies = serializers.SerializerMethodField()
    gallery = ProjectImageSerializer(many=True, read_only=True)
    features = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "slug",
            "summary",
            "description",
            "problem",
            "solution",
            "architecture",
            "challenges",
            "lessons_learned",
            "features",
            "image",
            "gallery",
            "github_url",
            "live_url",
            "case_study_url",
            "featured",
            "technologies",
            "created_at",
            "updated_at",
        ]

    def get_technologies(self, obj):
        return TechnologySerializer(
            [pt.technology for pt in obj.technologies.select_related("technology")], many=True
        ).data

    def get_features(self, obj):
        return obj.feature_list


class ExperienceSerializer(serializers.ModelSerializer):
    technologies = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = [
            "id",
            "position",
            "company",
            "company_url",
            "location",
            "description",
            "technologies",
            "start_date",
            "end_date",
            "is_current",
            "order",
        ]

    def get_technologies(self, obj):
        return obj.technology_list


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ["id", "institution", "degree", "description", "start_date", "end_date", "order"]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "title", "description", "icon", "order"]


class ContactMessageSerializer(serializers.ModelSerializer):
    """Serializer used to CREATE a message from the public contact form.
    'status' is intentionally read-only so the public API can never set it.
    """

    class Meta:
        model = ContactMessage
        fields = ["id", "name", "email", "subject", "message", "status", "created_at"]
        read_only_fields = ["id", "status", "created_at"]

    def validate_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters long.")
        return value.strip()

    def validate_subject(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Subject must be at least 3 characters long.")
        return value.strip()

    def validate_message(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Message must be at least 10 characters long.")
        return value.strip()
