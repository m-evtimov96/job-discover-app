from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django_resized import ResizedImageField

from JobDiscover.core.validators import validate_start_with_capital, validate_correct_bulstat
from JobDiscover.jobs_auth.managers import JobDiscoverUserManager


class JobDiscoverUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = JobDiscoverUserManager()


class CompanyProfile(models.Model):
    user = models.OneToOneField(JobDiscoverUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=2000, blank=True, null=True)
    bulstat = models.BigIntegerField(blank=True, null=True, validators=(validate_correct_bulstat,))
    website = models.CharField(max_length=100, blank=True, null=True)
    company_icon = ResizedImageField(
        size=[100, 100],
        crop=['middle', 'center'],
        quality=100,
        upload_to='jobs_auth/company_icons',
        blank=True,
        null=True,
        help_text="Use image with 100x100px/200x200px for best results.",
    )
    company_banner = ResizedImageField(
        size=[800, 300],
        crop=['middle', 'center'],
        quality=100,
        upload_to='jobs_auth/company_banners',
        blank=True,
        null=True,
        help_text="Use image with 800x300px for best results.",
    )


class ApplicantProfile(models.Model):
    user = models.OneToOneField(JobDiscoverUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=20, validators=(validate_start_with_capital,))
    last_name = models.CharField(max_length=20, validators=(validate_start_with_capital,))
    bio = models.TextField(blank=True, null=True, max_length=300)
    profile_image = ResizedImageField(
        size=[150, 200],
        crop=['middle', 'center'],
        quality=100,
        upload_to='jobs_auth/profile_pictures',
        blank=True,
        null=True,
        help_text="Use image with 150x200px/300x400px for best results.",
    )
