from django.urls import path

from JobDiscover.core.views import index, CompanyProfileView, ApplicantProfileView, EditCompanyView

urlpatterns = [
    path('', index, name='index'),
    path('profile-company/<int:pk>', CompanyProfileView.as_view(), name='company profile'),
    path('profile-company/edit/<int:pk>', EditCompanyView.as_view(), name='company edit'),
    path('profile-applicant/', ApplicantProfileView.as_view(), name='applicant profile'),
]