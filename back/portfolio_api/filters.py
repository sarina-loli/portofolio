import django_filters

from .models import Project, Skill


class ProjectFilter(django_filters.FilterSet):
    featured = django_filters.BooleanFilter(field_name="featured")
    technology = django_filters.CharFilter(
        field_name="technologies__technology__name",
        lookup_expr="iexact",
    )

    class Meta:
        model = Project
        fields = ["featured", "technology"]


class SkillFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name="category", lookup_expr="iexact")

    class Meta:
        model = Skill
        fields = ["category"]
