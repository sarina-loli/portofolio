from django.contrib import admin

from .models import (
    ContactMessage,
    Education,
    Experience,
    Profile,
    Project,
    ProjectImage,
    ProjectTechnology,
    Service,
    Skill,
    Technology,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "title", "email", "updated_at")
    fieldsets = (
        ("Identity", {"fields": ("full_name", "title", "tagline", "avatar", "resume")}),
        ("Content", {"fields": ("intro", "about", "philosophy", "specialties", "career_goals")}),
        ("Contact", {"fields": ("email", "phone", "location")}),
        ("Links", {"fields": ("github_url", "linkedin_url", "twitter_url","tiktok_url", "website_url")}),
        ("Stats", {"fields": ("years_experience",)}),
    )

    def has_add_permission(self, request):
        # Keep this a singleton: only allow adding a Profile if none exists yet.
        return not Profile.objects.exists()


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency", "order")
    list_filter = ("category",)
    list_editable = ("proficiency", "order")
    search_fields = ("name",)


class ProjectTechnologyInline(admin.TabularInline):
    model = ProjectTechnology
    extra = 1


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "order", "created_at")
    list_filter = ("featured",)
    list_editable = ("featured", "order")
    search_fields = ("title", "summary", "description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProjectTechnologyInline, ProjectImageInline]
    fieldsets = (
        (None, {"fields": ("title", "slug", "summary", "image", "featured", "order")}),
        ("Detail page content", {
            "fields": (
                "description",
                "problem",
                "solution",
                "architecture",
                "challenges",
                "lessons_learned",
                "features",
            )
        }),
        ("Links", {"fields": ("github_url", "live_url", "case_study_url")}),
    )


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name", "icon")
    search_fields = ("name",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("position", "company", "start_date", "end_date", "is_current", "order")
    list_editable = ("order",)
    list_filter = ("is_current",)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "start_date", "end_date", "order")
    list_editable = ("order",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "status", "created_at")
    list_filter = ("status", "created_at")
    list_editable = ("status",)
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("name", "email", "subject", "message", "created_at")

    def has_add_permission(self, request):
        # Messages only come in through the public contact form.
        return False
