from django.urls import path

from JobDiscover.core.views import index

urlpatterns = [
    path('', index, name='index'),
]