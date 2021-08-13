from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.db import transaction

from JobDiscover.core.forms import BootstrapFormMixin
from JobDiscover.jobs_auth.models import ApplicantProfile, CompanyProfile

UserModel = get_user_model()


class ApplicantRegisterForm(BootstrapFormMixin, UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta(UserCreationForm):
        model = UserModel
        fields = ('email',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_applicant = True
        user.save()
        applicant = ApplicantProfile.objects.create(user=user)
        applicant.first_name = self.cleaned_data.get('first_name')
        applicant.last_name = self.cleaned_data.get('last_name')
        applicant.save()
        return user


class CompanyRegisterForm(BootstrapFormMixin, UserCreationForm):
    name = forms.CharField()

    class Meta(UserCreationForm):
        model = UserModel
        fields = ('email',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.save()
        company = CompanyProfile.objects.create(user=user)
        company.name = self.cleaned_data.get('name')
        company.save()
        return user


class LogInForm(BootstrapFormMixin, AuthenticationForm):

    def save(self):
        return self.user
