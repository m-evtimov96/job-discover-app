from django.urls import path

from JobDiscover.jobs_auth.views import ApplicantRegisterView, CompanyRegisterView, log_out, RegisterView, LogInView

urlpatterns = (
    path('register/', RegisterView.as_view(), name='main register'),
    path('applicant-register/', ApplicantRegisterView.as_view(), name='applicant register'),
    path('company-register/', CompanyRegisterView.as_view(), name='company register'),
    path('log-in/', LogInView.as_view(), name='log in'),
    path('log-out/', log_out, name='log out'),
)
