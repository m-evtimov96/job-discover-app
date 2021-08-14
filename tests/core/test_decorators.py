from django.http import HttpResponse
from django.test import RequestFactory, TestCase

from JobDiscover.core.decorators import company_required, applicant_required
from JobDiscover.jobs_auth.models import JobDiscoverUser, CompanyProfile, ApplicantProfile


class CompanyRequiredTests(TestCase):
    def setUp(self):
        self.company_user = JobDiscoverUser(email='test@test.bg', password='test1234', is_company=True)
        self.company_user.save()

        self.other_user = JobDiscoverUser(email='test2@test.bg', password='test1234', is_company=False)
        self.other_user.save()

        self.factory = RequestFactory()

    def test_companyUser_ShouldGet200(self):
        @company_required
        def a_view(r):
            return HttpResponse()

        request = self.factory.get('/foo')
        request.user = self.company_user
        resp = a_view(request)
        self.assertEqual(resp.status_code, 200)

    def test_otherUser_ShouldGet302(self):
        @company_required
        def a_view(r):
            return HttpResponse()

        request = self.factory.get('/foo')
        request.user = self.other_user
        resp = a_view(request)
        self.assertEqual(resp.status_code, 302)


class ApplicantRequiredTests(TestCase):
    def setUp(self):
        self.applicant_user = JobDiscoverUser(email='test@test.bg', password='test1234', is_applicant=True)
        self.applicant_user.save()

        self.other_user = JobDiscoverUser(email='test2@test.bg', password='test1234', is_applicant=False)
        self.other_user.save()

        self.factory = RequestFactory()

    def test_companyUser_ShouldGet200(self):
        @applicant_required
        def a_view(r):
            return HttpResponse()

        request = self.factory.get('/foo')
        request.user = self.applicant_user
        resp = a_view(request)
        self.assertEqual(resp.status_code, 200)

    def test_otherUser_ShouldGet302(self):
        @applicant_required()
        def a_view(r):
            return HttpResponse()

        request = self.factory.get('/foo')
        request.user = self.other_user
        resp = a_view(request)
        self.assertEqual(resp.status_code, 302)
