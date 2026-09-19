from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class JobApplication(models.Model):

    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('offer', 'Offer'),
        ('rejected', 'Rejected'),
        ('withdrawn', 'Withdrawn'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    application_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='applied'
    )

    job_url = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    interview_date = models.DateField(
        null=True,
        blank=True
    )
