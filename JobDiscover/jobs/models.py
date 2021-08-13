from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django_resized import ResizedImageField
from multiselectfield import MultiSelectField

from JobDiscover.core.validators import validate_is_doc, validate_start_with_capital
from JobDiscover.jobs_auth.models import ApplicantProfile, CompanyProfile

UserModel = get_user_model()


class Job(models.Model):
    AUTOMOTIVE = 'automotive'
    ACCOUNTING = 'accounting'
    BANKING = 'banking'
    CALL_CENTER = 'call_center'
    CLEANING = 'cleaning'
    DRIVING = 'driving'
    DESIGN = 'design'
    EDUCATION = 'education'
    HEALTHCARE = 'healthcare'
    IT = 'it'
    LEGAL = 'legal'
    MANAGEMENT = 'management'
    MEDIA = 'media'
    RESTAURANTS = 'restaurants'
    SECURITY = 'security'

    CATEGORY_CHOICES = [
        (AUTOMOTIVE, 'Automotive, Auto Service'),
        (ACCOUNTING, 'Accounting, Finance'),
        (BANKING, 'Banking, Lending'),
        (CALL_CENTER, 'Call Center, Customer Support'),
        (CLEANING, 'Cleaning, Household Services'),
        (DRIVING, 'Drivers, Couriers'),
        (DESIGN, 'Design'),
        (EDUCATION, 'Education'),
        (HEALTHCARE, 'Healthcare, Pharmacy'),
        (IT, 'Information Technology, Development'),
        (LEGAL, 'Legal'),
        (MANAGEMENT, 'Management'),
        (MEDIA, 'Media, Publishing'),
        (RESTAURANTS, 'Restaurants, Hotels, Bars'),
        (SECURITY, 'Security'),
    ]

    FULL_TIME = 'full_time'
    FOR_STUDENTS = 'for_students'
    FREELANCE = 'freelance'
    INTERNSHIP = 'internship'
    LITTLE_EXPERIENCE = 'little_experience'
    PART_TIME = 'part_time'

    TYPE_CHOICES = [
        (FULL_TIME, 'Full Time'),
        (FOR_STUDENTS, 'For Students'),
        (FREELANCE, 'Freelance'),
        (INTERNSHIP, 'Internship'),
        (LITTLE_EXPERIENCE, 'Candidates with little or no experience'),
        (PART_TIME, 'Part Time'),
    ]

    title = models.CharField(max_length=75)
    description = models.TextField(max_length=5000)
    date_created = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=25, validators=(validate_start_with_capital,))
    type = MultiSelectField(choices=TYPE_CHOICES)
    salary = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1)])
    image = ResizedImageField(
        size=[800, 200],
        crop=['middle', 'center'],
        quality=100,
        upload_to='jobs',
        blank=True,
        null=True,
        help_text="Use image with 800x200px for best results.",
    )

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class Application(models.Model):
    motivational_letter = models.TextField(max_length=2000)
    cv = models.FileField(upload_to='applications', validators=(validate_is_doc,))
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(ApplicantProfile, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
