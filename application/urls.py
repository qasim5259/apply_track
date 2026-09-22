from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobApplicationList.as_view(), name='jobapplication_list'),
    path('add/', views.jobapplication_create, name='jobapplication_create'),
    path('<int:pk>/', views.jobapplication_detail, name='jobapplication_detail'),
]