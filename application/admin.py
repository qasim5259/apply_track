from django.contrib import admin
from .models import JobApplication
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(JobApplication)
class JobApplicationAdmin(SummernoteModelAdmin):

    list_display = ('company', 'job_title', 'status', 'application_date')
    search_fields = ['company', 'job_title']
    list_filter = ('status', 'application_date')
    summernote_fields = ('notes',)
