from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView
from JobDiscover.jobs_auth.forms import ApplicantRegisterForm, CompanyRegisterForm, LogInForm

UserModel = get_user_model()


class RegisterView(TemplateView):
    template_name = 'auth/register.html'


class ApplicantRegisterView(CreateView):
    template_name = 'auth/applicant-register.html'
    model = UserModel
    form_class = ApplicantRegisterForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'applicant'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class CompanyRegisterView(CreateView):
    template_name = 'auth/company-register.html'
    model = UserModel
    form_class = CompanyRegisterForm
    success_url = reverse_lazy('index')

    # TODO: Check if this logic is correct
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LogInView(LoginView):
    template_name = 'auth/log-in.html'
    form_class = LogInForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('index')


def log_out(request):
    logout(request)
    return redirect('index')
