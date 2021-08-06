from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from JobDiscover.jobs.forms import JobCreateForm
from JobDiscover.jobs.models import Job


class JobListView(ListView):
    template_name = 'jobs/job-list.html'
    model = Job
    context_object_name = 'jobs'
    paginate_by = 3


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
