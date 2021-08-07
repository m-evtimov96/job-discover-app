import os

from django.conf import settings
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView

from JobDiscover.jobs.forms import JobCreateForm, ApplicationCreateForm
from JobDiscover.jobs.models import Job, Application
from JobDiscover.jobs_auth.models import CompanyProfile


class JobListView(ListView):
    template_name = 'jobs/job-list.html'
    model = Job
    context_object_name = 'jobs'
    paginate_by = 10


class JobDetailView(DetailView):
    template_name = 'jobs/job-detail.html'
    model = Job


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
    #     TODO: Protect for logged applicants only


class ApplicationDetailView(DetailView):
    template_name = 'jobs/application-detail.html'
    model = Application
