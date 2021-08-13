from django.test import TestCase
from django.urls import reverse

from JobDiscover.jobs_auth.models import JobDiscoverUser, ApplicantProfile, CompanyProfile


class RegisterViewTests(TestCase):
    def test_viewUrlExistsAtDesiredLocation(self):
        response = self.client.get('/auth/register/')
        self.assertEqual(response.status_code, 200)

    def test_viewUrlAccessibleByName(self):
        response = self.client.get(reverse('main register'))
        self.assertEqual(response.status_code, 200)

    def test_viewUsesCorrectTemplate(self):
        response = self.client.get(reverse('main register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/register.html')


class ApplicantRegisterViewTests(TestCase):
    def test_viewUrlExistsAtDesiredLocation(self):
        response = self.client.get('/auth/applicant-register/')
        self.assertEqual(response.status_code, 200)

    def test_viewUrlAccessibleByName(self):
        response = self.client.get(reverse('applicant register'))
        self.assertEqual(response.status_code, 200)

    def test_viewUsesCorrectTemplate(self):
        response = self.client.get(reverse('applicant register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/applicant-register.html')

    def test_viewSavesUserAfterPost(self):
        self.client.post(reverse('applicant register'),
                         data={'email': 'test@test.bg',
                               'password1': 'strongandlongpassword',
                               'password2': 'strongandlongpassword',
                               'first_name': 'first',
                               'last_name': 'last'})
        self.assertEqual(JobDiscoverUser.objects.count(), 1)
        self.assertEqual(ApplicantProfile.objects.count(), 1)
        self.assertEqual(JobDiscoverUser.objects.first().id, ApplicantProfile.objects.first().user_id)


class CompanyRegisterView(TestCase):
    def test_viewUrlExistsAtDesiredLocation(self):
        response = self.client.get('/auth/company-register/')
        self.assertEqual(response.status_code, 200)

    def test_viewUrlAccessibleByName(self):
        response = self.client.get(reverse('company register'))
        self.assertEqual(response.status_code, 200)

    def test_viewUsesCorrectTemplate(self):
        response = self.client.get(reverse('company register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/company-register.html')

    def test_viewSavesUserAfterPost(self):
        self.client.post(reverse('company register'),
                         data={'email': 'test@test.bg',
                               'password1': 'strongandlongpassword',
                               'password2': 'strongandlongpassword',
                               'name': 'testname',})
        self.assertEqual(JobDiscoverUser.objects.count(), 1)
        self.assertEqual(CompanyProfile.objects.count(), 1)
        self.assertEqual(JobDiscoverUser.objects.first().id, CompanyProfile.objects.first().user_id)
