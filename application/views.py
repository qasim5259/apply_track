from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import JobApplication


# Create your views here.
class JobApplicationList(ListView):
    queryset = JobApplication.objects.all()
    template_name = "application/jobapplication_list.html"
    paginate_by = 6

def jobapplication_detail(request, pk):
    """
    Display an individual :model:`application.JobApplication`.
    """
    queryset = JobApplication.objects.all()
    application = get_object_or_404(queryset, pk=pk)

    return render(
        request,
        "application/jobapplication_detail.html",
        {
            "application": application,
        },
    )
