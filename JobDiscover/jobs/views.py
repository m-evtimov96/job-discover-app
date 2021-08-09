from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView
from django_filters.views import FilterView

from JobDiscover.core.decorators import company_required, applicant_required
from JobDiscover.core.mixins import IsOwnerMixin, BelongsToCompany
from JobDiscover.jobs.filters import JobFilter
from JobDiscover.jobs.forms import JobCreateForm, ApplicationCreateForm, JobEditForm
from JobDiscover.jobs.models import Job, Application
from JobDiscover.jobs_auth.models import CompanyProfile


class JobListView(FilterView):
    template_name = 'jobs/job-list.html'
    model = Job
    paginate_by = 10
    filterset_class = JobFilter
    ordering = ['-date_created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.copy()
        if 'page' in query:
            del query['page']
        context['filter'] = JobFilter(self.request.GET, queryset=self.get_queryset())
        context['queries'] = query
        return context


class JobDetailView(DetailView):
    template_name = 'jobs/job-detail.html'
    model = Job

    def get_context_data(self, **kwargs):
        context = super(JobDetailView, self).get_context_data(**kwargs)
        context['is_profile_owner'] = self.object.user_id == self.request.user.id
        return context


@method_decorator([login_required, company_required], name='dispatch')
class JobCreateView(CreateView):
    template_name = 'jobs/job-create.html'
    model = Job
    form_class = JobCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        job = form.save(commit=False)
        job.user = self.request.user
        job.save()
        return super(JobCreateView, self).form_valid(form)


class JobEditView(LoginRequiredMixin, IsOwnerMixin, UpdateView):
    template_name = 'jobs/job-edit.html'
    form_class = JobEditForm
    model = Job

    def get_success_url(self):
        return reverse('job detail', kwargs={'pk': self.object.pk})


def delete_job(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST' and request.user.id == job.user.id:
        job.delete()
        return redirect('job list')
    else:
        raise Http404('Page not found')


@method_decorator([login_required, applicant_required], name='dispatch')
class ApplicationCreateView(CreateView):
    template_name = 'jobs/application-create.html'
    model = Application
    form_class = ApplicationCreateForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(ApplicationCreateView, self).get_context_data(**kwargs)
        context['job'] = self.get_application_job()
        return context

    def form_valid(self, form):
        application = form.save(commit=False)
        application.applicant = self.request.user.applicantprofile
        application.job = self.get_application_job()
        application.company = CompanyProfile.objects.get(user=application.job.user)
        application.save()
        return super(ApplicationCreateView, self).form_valid(form)

    def get_application_job(self):
        application_job = Job.objects.get(pk=self.kwargs['pk'])
        return application_job


class ApplicationDetailView(BelongsToCompany, DetailView):
    template_name = 'jobs/application-detail.html'
    model = Application
