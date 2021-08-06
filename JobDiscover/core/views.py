from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from JobDiscover.core.forms import EditCompanyForm
from JobDiscover.jobs.models import Job
from JobDiscover.jobs_auth.models import CompanyProfile, ApplicantProfile


def index(request):
    return render(request, 'core/index.html')


class CompanyProfileView(DetailView):
    template_name = 'core/company-profile.html'
    model = CompanyProfile

    def get_context_data(self, **kwargs):
        context = super(CompanyProfileView, self).get_context_data(**kwargs)
        context['is_profile_owner'] = self.object.pk == self.request.user.id
        context['jobs_list'] = Job.objects.filter(user_id=self.object.pk)
        return context


class EditCompanyView(UpdateView):
    template_name = 'core/company-edit.html'
    form_class = EditCompanyForm
    model = CompanyProfile
    success_url = reverse_lazy('index')


class ApplicantProfileView(DetailView):
    template_name = 'core/applicant-profile.html'
    model = ApplicantProfile
#     Add more
