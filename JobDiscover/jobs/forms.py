from django import forms

from JobDiscover.core.forms import BootstrapFormMixin
from JobDiscover.jobs.models import Job, Application


class JobCreateForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'date_created')


class ApplicationCreateForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Application
        exclude = ('job', 'applicant', 'company')

