from django.urls import path

from JobDiscover.jobs_auth.views import ApplicantRegisterView, CompanyRegisterView, log_out

urlpatterns = (
    path('ApplicantRegister/', ApplicantRegisterView.as_view(), name='applicant register'),
    path('CompanyRegister/', CompanyRegisterView.as_view(), name='company register'),
    path('Log-out/', log_out, name='log out'),
)