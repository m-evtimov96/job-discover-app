from django import forms
from JobDiscover.core.forms import BootstrapFormMixin
from JobDiscover.core.validators import file_size
from JobDiscover.jobs.models import Job, Application


class JobCreateForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'date_created')

    def clean_image(self):
        image = self.cleaned_data.get('image')
        file_size(image)
        return image


class JobEditForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'date_created')

    def clean_image(self):
        image = self.cleaned_data.get('image')
        file_size(image)
        return image


class ApplicationCreateForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Application
        exclude = ('job', 'applicant', 'company')
