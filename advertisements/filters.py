import django_filters
from django_filters import rest_framework as filters

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at_before = django_filters.DateFromToRangeFilter()
    # status = django_filters.ChoiceFilter(choices=AdvertisementStatusChoices)

    class Meta:
        model = Advertisement
        fields = '__all__'
