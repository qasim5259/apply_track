from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .forms import JobApplicationForm
from .models import JobApplication


class JobApplicationList(LoginRequiredMixin, ListView):
    model = JobApplication
    template_name = "application/jobapplication_list.html"
    paginate_by = 6

    def get_queryset(self):
        # Filter applications so users only see their own records
        return JobApplication.objects.filter(
            user=self.request.user
        ).order_by('-application_date')


@login_required
def jobapplication_detail(request, pk):
    """
    Display an individual :model:`application.JobApplication`.
    """
    # Ensure users can only access their own application detail page
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)
    return render(
        request,
        "application/jobapplication_detail.html",
        {"application": application},
    )


@login_required
def jobapplication_create(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('jobapplication_list')
    else:
        form = JobApplicationForm()

    return render(
        request,
        'application/jobapplication_form.html',
        {'form': form},
    )


@login_required
def jobapplication_update(request, pk):
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('jobapplication_list')
    else:
        form = JobApplicationForm(instance=application)

    return render(
        request,
        'application/jobapplication_form.html',
        {'form': form, 'edit_mode': True},
    )


@login_required
def jobapplication_delete(request, pk):
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)
    if request.method == 'POST':
        application.delete()
        return redirect('jobapplication_list')

    return render(
        request,
        'application/jobapplication_confirm_delete.html',
        {'application': application},
    )


def home(request):
    if request.user.is_authenticated:
        return redirect('jobapplication_list')
    return render(request, 'application/home.html')
