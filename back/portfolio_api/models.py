from django.core.validators import RegexValidator
from django.db import models
from django.utils.text import slugify


class Profile(models.Model):
    """Singleton-ish model holding the developer's headline info.
    Managed entirely from Django admin; the frontend fetches /api/profile/.
    """

    full_name = models.CharField(max_length=120)
    title = models.CharField(max_length=150, default="Full-Stack Software Developer")
    tagline = models.CharField(max_length=250, blank=True)
    intro = models.TextField(help_text="Short hero introduction paragraph.")
    about = models.TextField(help_text="Longer 'About Me' narrative.")
    philosophy = models.TextField(blank=True, help_text="Development philosophy.")
    specialties = models.TextField(blank=True, help_text="What I specialize in.")
    career_goals = models.TextField(blank=True)
    location = models.CharField(max_length=120, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(upload_to="profile/", blank=True, null=True)
    resume = models.FileField(upload_to="resume/", blank=True, null=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    tiktok_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)
    hello = models.TextField(blank=True)
    years_experience = models.PositiveSmallIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    class Category(models.TextChoices):
        FRONTEND = "frontend", "Frontend"
        BACKEND = "backend", "Backend"
        DATABASE = "database", "Database"
        SECURITY = "security", "Authentication & Security"
        TOOLS = "tools", "Tools & Deployment"
        OTHER = "other", "Other"

    name = models.CharField(max_length=80)
    category = models.CharField(max_length=20, choices=Category.choices)
    icon = models.CharField(
        max_length=60,
        blank=True,
        help_text="Icon identifier (e.g. an icon-library key like 'react' or 'python').",
    )
    proficiency = models.PositiveSmallIntegerField(
        default=80,
        help_text="0-100, optional editable proficiency indicator.",
    )
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["category", "order", "name"]

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True, blank=True)
    summary = models.CharField(max_length=300, help_text="Short card-view description.")
    description = models.TextField(help_text="Full description for the project detail page.")
    problem = models.TextField(blank=True, help_text="The problem this project solves.")
    solution = models.TextField(blank=True, help_text="How the project solves it.")
    architecture = models.TextField(blank=True, help_text="High-level architecture notes.")
    challenges = models.TextField(blank=True)
    lessons_learned = models.TextField(blank=True)
    features = models.TextField(
        blank=True,
        help_text="One feature per line; rendered as a bullet list.",
    )
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    case_study_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-featured", "order", "-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def feature_list(self):
        return [f.strip() for f in self.features.splitlines() if f.strip()]


class Technology(models.Model):
    """A reusable technology/tag (React, Django, PostgreSQL, ...)."""

    name = models.CharField(max_length=60, unique=True)
    icon = models.CharField(max_length=60, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class ProjectTechnology(models.Model):
    """Through model linking a Project to a Technology, per the spec's
    'Project technologies' resource."""

    project = models.ForeignKey(Project, related_name="technologies", on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, related_name="project_links", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("project", "technology")

    def __str__(self):
        return f"{self.project.title} — {self.technology.name}"


class ProjectImage(models.Model):
    """Optional extra screenshots for a project's detail page/gallery."""

    project = models.ForeignKey(Project, related_name="gallery", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="projects/gallery/")
    caption = models.CharField(max_length=150, blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"Image for {self.project.title}"


class Experience(models.Model):
    position = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    company_url = models.URLField(blank=True)
    location = models.CharField(max_length=120, blank=True)
    description = models.TextField()
    technologies = models.CharField(
        max_length=300,
        blank=True,
        help_text="Comma-separated list of technologies used.",
    )
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if current.")
    is_current = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "-start_date"]

    def __str__(self):
        return f"{self.position} @ {self.company}"

    @property
    def technology_list(self):
        return [t.strip() for t in self.technologies.split(",") if t.strip()]


class Education(models.Model):
    institution = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "-start_date"]
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} — {self.institution}"


class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    icon = models.CharField(max_length=60, blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


phone_validator = RegexValidator(
    regex=r"^[\d\s()+\-]{7,20}$",
    message="Enter a valid phone number.",
)


class ContactMessage(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "New"
        READ = "read", "Read"
        REPLIED = "replied", "Replied"
        ARCHIVED = "archived", "Archived"

    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.NEW)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.subject} — {self.name}"
