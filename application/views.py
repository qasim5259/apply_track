from django.shortcuts import render
from django.views.generic import ListView
from .models import JobApplication


# Create your views here.
class JobApplicationList(ListView):
    queryset = JobApplication.objects.all()
    template_name = "application/jobapplication_list.html"
    paginate_by = 6

