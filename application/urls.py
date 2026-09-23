from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('applications/', views.JobApplicationList.as_view(), name='jobapplication_list'),
    path('add/', views.jobapplication_create, name='jobapplication_create'),
    path('<int:pk>/', views.jobapplication_detail, name='jobapplication_detail'),
    path('<int:pk>/edit/', views.jobapplication_update, name='jobapplication_update'),
    path('<int:pk>/delete/', views.jobapplication_delete, name='jobapplication_delete'),
]