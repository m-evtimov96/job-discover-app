from django.urls import path

from JobDiscover.jobs.views import JobListView, JobDetailView, JobCreateView, ApplicationCreateView, \
    ApplicationDetailView, JobEditView, delete_job

urlpatterns = [
    path('', JobListView.as_view(), name='job list'),
    path('<int:pk>', JobDetailView.as_view(), name='job detail'),
    path('create/', JobCreateView.as_view(), name='job create'),
    path('edit/<int:pk>', JobEditView.as_view(), name='job edit'),
    path('delete/<int:pk>', delete_job, name='job delete'),
    path('<int:pk>/apply/', ApplicationCreateView.as_view(), name='application create'),
    path('application/<int:pk>', ApplicationDetailView.as_view(), name='application detail'),
]