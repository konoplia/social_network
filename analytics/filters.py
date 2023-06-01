import django_filters

from blog.models import Reaction


class FilterByLikeDate(django_filters.FilterSet):
    class Meta:
        model = Reaction
        fields = {
            'like_date': ['lte', 'gte']
        }
