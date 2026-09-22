from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'company',
            'job_title',
            'location',
            'application_date',
            'status',
            'job_url',
            'notes',
            'interview_date',
        ]
        widgets = {
            'application_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'interview_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'job_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }