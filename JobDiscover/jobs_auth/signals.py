from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from JobDiscover.jobs_auth.models import ApplicantProfile, CompanyProfile

UserModel = get_user_model()


# TODO: Not used now all logic for creation is in forms/views

# @receiver(post_save, sender=UserModel)
# def user_created(sender, instance, created, **kwargs):
#     if created:
#         if instance.is_applicant:
#             profile = ApplicantProfile(user=instance)
#             profile.save()
#         elif instance.is_company:
#             profile = CompanyProfile(user=instance)
#             profile.save()
