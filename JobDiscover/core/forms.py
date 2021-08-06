from django import forms

from JobDiscover.jobs_auth.models import CompanyProfile


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