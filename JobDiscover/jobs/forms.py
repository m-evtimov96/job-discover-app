from django import forms

from JobDiscover.core.forms import BootstrapFormMixin
from JobDiscover.jobs.models import Job


class JobCreateForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'date_created')

