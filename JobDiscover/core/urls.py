from django.urls import path

from JobDiscover.core.views import IndexView, CompanyProfileView, ApplicantProfileView, CompanyEditView, ApplicantEditView, \
    CompanyListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('profile-company/<int:pk>', CompanyProfileView.as_view(), name='company profile'),
    path('profile-company/edit/<int:pk>', CompanyEditView.as_view(), name='company edit'),
    path('profile-applicant/<int:pk>', ApplicantProfileView.as_view(), name='applicant profile'),
    path('profile-applicant/edit/<int:pk>', ApplicantEditView.as_view(), name='applicant edit'),
    path('companies/', CompanyListView.as_view(), name='company list'),
]