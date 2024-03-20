import django_filters
from django_filters.rest_framework.filterset import FilterSet


class NutrientFilterSet(FilterSet):
    food_name = django_filters.CharFilter(
        field_name="food_name", lookup_expr="icontains"
    )
    research_year = django_filters.CharFilter(
        field_name="research_year", lookup_expr="icontains"
    )
    maker_name = django_filters.CharFilter(
        field_name="maker_name", lookup_expr="icontains"
    )
    food_code = django_filters.CharFilter(
        field_name="food_cd", lookup_expr="icontains"
    )
