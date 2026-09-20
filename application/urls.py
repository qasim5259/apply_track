from django.urls import path
from .views import JobApplicationList

urlpatterns = [
    path('', JobApplicationList.as_view(), name='home'),
]