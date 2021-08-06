from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator, MaxLengthValidator
from django.db import models
from django_resized import ResizedImageField

from JobDiscover.jobs_auth.managers import JobDiscoverUserManager


class JobDiscoverUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = JobDiscoverUserManager()

# TODO: Make checker function for IsCompany and IsApplicant


class CompanyProfile(models.Model):
    user = models.OneToOneField(JobDiscoverUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=45)
    description = models.TextField(blank=True, null=True)
    bulstat = models.IntegerField(blank=True, null=True)
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

# TODO: Add website field


class ApplicantProfile(models.Model):
    user = models.OneToOneField(JobDiscoverUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profile_image = ResizedImageField(
        size=[150, 200],
        crop=['middle', 'center'],
        quality=100,
        upload_to='jobs_auth/profile_pictures',
        blank=True,
        null=True,
        help_text="Use image with 150x200px/300x400px for best results.",
    )

# TODO: Maybe add option to store CV's -> CV model linked to profile
