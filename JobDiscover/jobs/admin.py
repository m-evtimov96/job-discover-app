from django.contrib import admin
from JobDiscover.jobs.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    list_filter = ('user', 'category')
