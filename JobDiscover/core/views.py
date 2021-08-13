from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, ListView

from JobDiscover.core.forms import EditCompanyForm, EditApplicantForm
from JobDiscover.jobs.models import Job, Application
from JobDiscover.jobs_auth.models import CompanyProfile, ApplicantProfile


class IndexView(ListView):
    template_name = 'core/index.html'
    model = Job
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            return qs.filter(title__icontains=query)
        return qs

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'company_list': CompanyProfile.objects.order_by('name'),
        })
        query = self.request.GET.copy()
        if 'page' in query:
            del query['page']
        context['queries'] = query
        context['job_count'] = Job.objects.all().count()
        return context


class CompanyProfileView(DetailView):
    template_name = 'core/company-profile.html'
    model = CompanyProfile

    def get_context_data(self, **kwargs):
        context = super(CompanyProfileView, self).get_context_data(**kwargs)
        context['is_profile_owner'] = self.object.pk == self.request.user.id
        context['jobs_list'] = self.get_job_list()
        context['application_list'] = self.get_application_list()
        return context

    def get_job_list(self):
        job_list = Job.objects.filter(user_id=self.object.pk)
        return job_list

    def get_application_list(self):
        application_list = Application.objects.filter(company_id=self.object.pk)
        return application_list


class CompanyEditView(UpdateView):
    template_name = 'core/company-edit.html'
    form_class = EditCompanyForm
    model = CompanyProfile

    def get_success_url(self):
        return reverse('company profile', kwargs={'pk': self.object.pk})

    def get(self, request, *args, **kwargs):
        if not request.user.id == self.kwargs.get('pk'):
            return HttpResponseForbidden()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not request.user.id == self.kwargs.get('pk'):
            return HttpResponseForbidden()
        return super().post(request, *args, **kwargs)


class ApplicantProfileView(DetailView):
    template_name = 'core/applicant-profile.html'
    model = ApplicantProfile

    def get_context_data(self, **kwargs):
        context = super(ApplicantProfileView, self).get_context_data(**kwargs)
        context['is_profile_owner'] = self.object.pk == self.request.user.id
        return context

    def get(self, request, *args, **kwargs):
        if not request.user.id == self.kwargs.get('pk'):
            return HttpResponseForbidden()
        return super().get(request, *args, **kwargs)


class ApplicantEditView(UpdateView):
    template_name = 'core/applicant-edit.html'
    form_class = EditApplicantForm
    model = ApplicantProfile

    def get_success_url(self):
        return reverse('applicant profile', kwargs={'pk': self.object.pk})

    def get(self, request, *args, **kwargs):
        if not request.user.id == self.kwargs.get('pk'):
            return HttpResponseForbidden()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not request.user.id == self.kwargs.get('pk'):
            return HttpResponseForbidden()
        return super().post(request, *args, **kwargs)


class CompanyListView(ListView):
    template_name = 'core/company-list.html'
    model = CompanyProfile
    context_object_name = 'companies'
    paginate_by = 9
