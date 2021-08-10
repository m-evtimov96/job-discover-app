from django.contrib import admin
from JobDiscover.jobs.models import Job, Application


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    list_filter = ('user', 'category')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant',)