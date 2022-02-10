from django.urls import path
from django.contrib.auth import views as auth_views

from JobDiscover.jobs_auth.views import ApplicantRegisterView, CompanyRegisterView, log_out, RegisterView, LogInView

urlpatterns = (
    path('register/', RegisterView.as_view(), name='main register'),
    path('applicant-register/', ApplicantRegisterView.as_view(), name='applicant register'),
    path('company-register/', CompanyRegisterView.as_view(), name='company register'),
    path('log-in/', LogInView.as_view(), name='log in'),
    path('log-out/', log_out, name='log out'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='auth/password-reset.html'), name='reset_password'),
    path('password-reset-sent/', auth_views.PasswordResetDoneView.as_view(template_name='auth/password-reset-sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='auth/password-reset-form.html'), name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name='auth/password-reset-complete.html'), name='password_reset_complete'),
)
