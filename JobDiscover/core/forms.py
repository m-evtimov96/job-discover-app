from django import forms

from JobDiscover.core.validators import validate_image_file_size
from JobDiscover.jobs_auth.models import CompanyProfile, ApplicantProfile


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_fields()

    def _init_bootstrap_fields(self):
        fields = self.fields.items()
        for (name, field) in fields:
            if name != 'type':
                if 'class' not in field.widget.attrs:
                    field.widget.attrs['class'] = ''
                field.widget.attrs['class'] += ' form-control'


class EditCompanyForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = CompanyProfile
        exclude = ('user', 'name')

    def clean_company_icon(self):
        icon = self.cleaned_data.get('company_icon')
        validate_image_file_size(icon)
        return icon

    def clean_company_banner(self):
        banner = self.cleaned_data.get('company_banner')
        validate_image_file_size(banner)
        return banner


class EditApplicantForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = ApplicantProfile
        exclude = ('user',)

    def clean_profile_image(self):
        image = self.cleaned_data.get('profile_image')
        validate_image_file_size(image)
        return image