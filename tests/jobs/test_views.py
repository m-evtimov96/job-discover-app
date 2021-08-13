from django.http import Http404
from django.test import TestCase
from django.urls import reverse

from JobDiscover.jobs.models import Job, Application
from JobDiscover.jobs_auth.models import JobDiscoverUser, CompanyProfile, ApplicantProfile


class JobListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_jobs = 11

        test_user = JobDiscoverUser(email='test@test.bg', password='test1234', )
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

        Job.objects.create(
            title='testTitle',
            description='testDescr',
            category='LEGAL',
            location='Burgas',
            type='FULL_TIME',
            user=test_user,
        )

    def test_viewUrlExistsAtDesiredLocation(self):
        response = self.client.get('/jobs/')
        self.assertEqual(response.status_code, 200)

    def test_viewUrlAccessibleByName(self):
        response = self.client.get(reverse('job list'))
        self.assertEqual(response.status_code, 200)

    def test_viewUsesCorrectTemplate(self):
        response = self.client.get(reverse('job list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobs/job-list.html')

    def test_paginationIsTen(self):
        response = self.client.get(reverse('job list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['object_list']), 10)

    def test_listsAllJobs(self):
        response = self.client.get(reverse('job list') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['object_list']), 1)


class JobDetailViewTests(TestCase):
    def setUp(self):
        self.company_user = JobDiscoverUser(email='test@test.bg', password='test1234')
        self.company_user.save()

        self.company_profile = CompanyProfile(user=self.company_user, name='test_name')
        self.company_profile.save()

        self.test_job = Job(
            title='testTitle',
            description='testDescr',
            category='LEGAL',
            location='Burgas',
            type='FULL_TIME',
            user=self.company_user,
        )
        self.test_job.save()

    def test_viewUrlExistsAtDesiredLocation(self):
        response = self.client.get('/jobs/' + str(self.test_job.id))
        self.assertEqual(response.status_code, 200)

    def test_viewUrlAccessibleByName(self):
        response = self.client.get(reverse('job detail', kwargs={'pk': self.test_job.id}))
        self.assertEqual(response.status_code, 200)

    def test_viewUsesCorrectTemplate(self):
        response = self.client.get(reverse('job detail', kwargs={'pk': self.test_job.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobs/job-detail.html')

    def test_contextIsProfileOwnerWhenOwner_shouldReturnTrue(self):
        self.client.force_login(self.company_user)
        response = self.client.get(reverse('job detail', kwargs={'pk': self.test_job.id}))
        self.assertTrue(response.context['is_profile_owner'])

    def test_contextIsProfileOwnerWhenNotOwner_shouldReturnFalse(self):
        response = self.client.get(reverse('job detail', kwargs={'pk': self.test_job.id}))
        self.assertFalse(response.context['is_profile_owner'])


class JobCreateViewTests(TestCase):
    def setUp(self):
        self.company_user = JobDiscoverUser(email='test@test.bg', password='test1234')
        self.company_user.save()

        self.company_profile = CompanyProfile(user=self.company_user, name='test_name')
        self.company_profile.save()

        self.test_job = Job(
            title='testTitle',
            description='testDescr',
            category='LEGAL',
            location='Burgas',
            type='FULL_TIME',
            user=self.company_user,
        )
        self.test_job.save()

    def test_viewUrlExistsAtDesiredLocation(self):
        self.client.force_login(self.company_user)
        response = self.client.get('/jobs/create/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_viewUrlAccessibleByName(self):
        self.client.force_login(self.company_user)
        response = self.client.get(reverse('job create'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_createdJob(self):
        response = self.client.get(reverse('job detail', kwargs={'pk': self.test_job.id}))
        self.assertContains(response, "testTitle")

    def test_userIsSavedCorrectly(self):
        response = self.client.get(reverse('job detail', kwargs={'pk': self.test_job.id}))
        self.assertEqual(response.context['object'].user.email, 'test@test.bg')


class JobEditViewTests(TestCase):
    def setUp(self):
        self.company_user = JobDiscoverUser(email='test@test.bg', password='test1234')
        self.company_user.save()

        self.company_profile = CompanyProfile(user=self.company_user, name='test_name')
        self.company_profile.save()

        self.test_job = Job(
            title='testTitle',
            description='testDescr',
            category='LEGAL',
            location='Burgas',
            type='FULL_TIME',
            user=self.company_user,
        )
        self.test_job.save()

    def test_viewUrlExistsAtDesiredLocation(self):
        self.client.force_login(self.company_user)
        response = self.client.get('/jobs/edit/' + str(self.test_job.id))
        self.assertEqual(response.status_code, 200)

    def test_viewUrlAccessibleByName(self):
        self.client.force_login(self.company_user)
        response = self.client.get(reverse('job edit',  kwargs={'pk': self.test_job.id}))
        self.assertEqual(response.status_code, 200)

    def test_viewUsesCorrectTemplate(self):
        self.client.force_login(self.company_user)
        response = self.client.get(reverse('job edit', kwargs={'pk': self.test_job.id}))
        self.assertTemplateUsed(response, 'jobs/job-edit.html')


class DeleteJobTests(TestCase):
    def setUp(self):
        self.company_user = JobDiscoverUser(email='test@test.bg', password='test1234')
        self.company_user.save()

        self.company_profile = CompanyProfile(user=self.company_user, name='test_name')
        self.company_profile.save()

        self.test_job = Job(
            title='testTitle',
            description='testDescr',
            category='LEGAL',
            location='Burgas',
            type='FULL_TIME',
            user=self.company_user,
        )
        self.test_job.save()

    def test_tryToDeleteOnPostAndOwner_shouldSucceed(self):
        self.client.force_login(self.company_user)
        self.client.post('/jobs/delete/' + str(self.test_job.id))
        self.assertEqual(len(Job.objects.all()), 0)

    def test_tryToDeleteOnPostNotOwner_shouldRaise404(self):
        response = self.client.post('/jobs/delete/' + str(self.test_job.id))
        self.assertEqual(response.status_code, 404)

    def test_tryToDeleteOnGet_shouldRaise404(self):
        response = self.client.get('/jobs/delete/' + str(self.test_job.id))
        self.assertEqual(response.status_code, 404)

    def test_tryToDeleteOnGetAndOwner_shouldRaise404(self):
        self.client.force_login(self.company_user)
        response = self.client.get('/jobs/delete/' + str(self.test_job.id))
        self.assertEqual(response.status_code, 404)


class ApplicationCreateViewTests(TestCase):
    def setUp(self):
        self.company_user = JobDiscoverUser(email='test@test.bg', password='test1234')
        self.company_user.save()

        self.company_profile = CompanyProfile(user=self.company_user, name='test_name')
        self.company_profile.save()

        self.applicant_user = JobDiscoverUser(email='test2@test.bg', password='test1234')
        self.applicant_user.save()

        self.applicant_profile = ApplicantProfile(user=self.applicant_user, first_name='first', last_name='last')
        self.applicant_profile.save()

        self.test_job = Job(
            title='testTitle',
            description='testDescr',
            category='LEGAL',
            location='Burgas',
            type='FULL_TIME',
            user=self.company_user,
        )
        self.test_job.save()

    def test_viewUrlExistsAtDesiredLocation(self):
        self.client.force_login(self.applicant_user)
        response = self.client.get('/jobs/' + str(self.test_job.id) + '/apply/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_viewUrlAccessibleByName(self):
        self.client.force_login(self.applicant_user)
        response = self.client.get(reverse('application create',  kwargs={'pk': self.test_job.id}), follow=True)
        self.assertEqual(response.status_code, 200)

