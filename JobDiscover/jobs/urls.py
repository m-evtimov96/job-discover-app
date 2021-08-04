from django.urls import path

from JobDiscover.jobs.views import JobListView, JobDetailView, JobCreateView

urlpatterns = [
    path('', JobListView.as_view(), name='list jobs'),
    path('<int:pk>', JobDetailView.as_view(), name='detail job'),
    path('create/', JobCreateView.as_view(), name='create job'),
]