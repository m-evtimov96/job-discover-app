import django_filters

from JobDiscover.jobs.models import Job


class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = {
            'category': ['exact'],
            'salary': ['gt', 'lt'],
        }
