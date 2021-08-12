from django.test import TestCase
from django.urls import reverse

from JobDiscover.jobs.models import Job, Application
from JobDiscover.jobs_auth.models import JobDiscoverUser, CompanyProfile, ApplicantProfile


class IndexViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_jobs = 7

        test_user = JobDiscoverUser(
            email='test@test.bg',
            password='test1234',
        )
        test_user.save()

        for job_id in range(number_of_jobs):
            Job.objects.create(
                title=f'Title {job_id}',
                description=f'Description {job_id}',
                category='IT',
                location='Sofia',
                type='FULL_TIME',
                user=test_user,
            )

    def test_viewUrlExistsAtDesiredLocation(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_viewUrlAccessibleByName(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_viewUsesCorrectTemplate(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')

    def test_paginationIsFive(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['object_list']), 5)

    def test_listsAllJobs(self):
        response = self.client.get(reverse('index') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['object_list']), 2)

    def test_getQuerySetWorks(self):
        response = self.client.get(reverse('index') + '?q=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 1)


class CompanyProfileViewTests(TestCase):
    def setUp(self):
        self.company_user = JobDiscoverUser(email='test@test.bg', password='test1234')
        self.company_user.save()

        self.company_profile = CompanyProfile(user=self.company_user, name='test')
        self.company_profile.save()

        self.applicant_user = JobDiscoverUser(email='test@test2.bg', password='test12345')
        self.applicant_user.save()

        self.applicant_profile = ApplicantProfile(user=self.applicant_user, first_name='first', last_name='last')
        self.applicant_profile.save()

        self.test_job = Job(
            title='Title',
            description='Description',
            category='IT',
            location='Sofia',
            type='FULL_TIME',
            user=self.company_user,
        )
        self.test_job.save()

        self.test_appl = Application(
            motivational_letter='letter',
            cv='test.pdf',
            job=self.test_job,
            applicant=self.applicant_profile,
            company=self.company_profile,
        )
        self.test_appl.save()

        self.test_appl2 = Application(
            motivational_letter='letter2',
            cv='test2.pdf',
            job=self.test_job,
            applicant=self.applicant_profile,
            company=self.company_profile,
        )
        self.test_appl2.save()

    def test_viewUrlAccessibleByName(self):
        response = self.client.get(reverse('company profile', kwargs={'pk': self.company_user.id}))
        self.assertEqual(response.status_code, 200)

    def test_viewUsesCorrectTemplate(self):
        response = self.client.get(reverse('company profile', kwargs={'pk': self.company_user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/company-profile.html')

    def test_getJobListWorks(self):
        response = self.client.get(reverse('company profile', kwargs={'pk': self.company_user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['jobs_list']), 1)

    def test_getApplicationListWorks(self):
        response = self.client.get(reverse('company profile', kwargs={'pk': self.company_user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['application_list']), 2)


class CompanyEditViewTests(TestCase):
    def setUp(self):
        self.company_user = JobDiscoverUser(email='test@test.bg', password='test1234')
        self.company_user.save()

        self.company_profile = CompanyProfile(user=self.company_user, name='test')
        self.company_profile.save()

    def test_viewUrlAccessibleByName(self):
        self.client.force_login(self.company_user)
        response = self.client.get(reverse('company edit', kwargs={'pk': self.company_user.id}))
        self.assertEqual(response.status_code, 200)

    def test_viewUsesCorrectTemplate(self):
        self.client.force_login(self.company_user)
        response = self.client.get(reverse('company edit', kwargs={'pk': self.company_user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/company-edit.html')

    def test_userIsNotProfileOwner_getShouldReturn403(self):
        response = self.client.get(reverse('company edit', kwargs={'pk': self.company_user.id}))
        self.assertEqual(response.status_code, 403)

    def test_userIsNotProfileOwner_postShouldReturn403(self):
        response = self.client.post(reverse('company edit', kwargs={'pk': self.company_user.id}))
        self.assertEqual(response.status_code, 403)


class ApplicantProfileViewTests(TestCase):
    def setUp(self):
        self.applicant_user = JobDiscoverUser(email='test@test.bg', password='test1234')
        self.applicant_user.save()

        self.applicant_profile = ApplicantProfile(user=self.applicant_user, first_name='first', last_name='last')
        self.applicant_profile.save()

    def test_viewUrlAccessibleByName(self):
        self.client.force_login(self.applicant_user)
        response = self.client.get(reverse('applicant profile', kwargs={'pk': self.applicant_user.id}))
        self.assertEqual(response.status_code, 200)

    def test_viewUsesCorrectTemplate(self):
        self.client.force_login(self.applicant_user)
        response = self.client.get(reverse('applicant profile', kwargs={'pk': self.applicant_user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/applicant-profile.html')

    def test_userIsNotProfileOwner_getShouldReturn403(self):
        response = self.client.get(reverse('applicant profile', kwargs={'pk': self.applicant_user.id}))
        self.assertEqual(response.status_code, 403)

    def test_contextIsProfileOwnerWhenOwner_shouldReturnTrue(self):
        self.client.force_login(self.applicant_user)
        response = self.client.get(reverse('applicant profile', kwargs={'pk': self.applicant_user.id}))
        self.assertTrue(response.context['is_profile_owner'])


class ApplicantEditViewTests(TestCase):
    def setUp(self):
        self.applicant_user = JobDiscoverUser(email='test@test.bg', password='test1234')
        self.applicant_user.save()

        self.applicant_profile = ApplicantProfile(user=self.applicant_user, first_name='first', last_name='last')
        self.applicant_profile.save()

    def test_viewUrlAccessibleByName(self):
        self.client.force_login(self.applicant_user)
        response = self.client.get(reverse('applicant edit', kwargs={'pk': self.applicant_user.id}))
        self.assertEqual(response.status_code, 200)

    def test_viewUsesCorrectTemplate(self):
        self.client.force_login(self.applicant_user)
        response = self.client.get(reverse('applicant edit', kwargs={'pk': self.applicant_user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/applicant-edit.html')

    def test_userIsNotProfileOwner_getShouldReturn403(self):
        response = self.client.get(reverse('applicant edit', kwargs={'pk': self.applicant_user.id}))
        self.assertEqual(response.status_code, 403)

    def test_userIsNotProfileOwner_postShouldReturn403(self):
        response = self.client.post(reverse('applicant edit', kwargs={'pk': self.applicant_user.id}))
        self.assertEqual(response.status_code, 403)


class CompanyListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_companies = 10

        for company_id in range(number_of_companies):
            company_user = JobDiscoverUser(email=f'test@test.bg {company_id}', password=f'test1234 {company_id}')
            company_user.save()
            company_profile = CompanyProfile(user=company_user, name='testtitle')
            company_profile.save()

    def test_viewUrlExistsAtDesiredLocation(self):
        response = self.client.get('/companies/')
        self.assertEqual(response.status_code, 200)

    def test_viewUrlAccessibleByName(self):
        response = self.client.get(reverse('company list'))
        self.assertEqual(response.status_code, 200)

    def test_viewUsesCorrectTemplate(self):
        response = self.client.get(reverse('company list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/company-list.html')

    def test_paginationIsFive(self):
        response = self.client.get(reverse('company list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['object_list']), 9)

    def test_listsAllJobs(self):
        response = self.client.get(reverse('company list') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['object_list']), 1)