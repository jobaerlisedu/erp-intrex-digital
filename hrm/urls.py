from django.urls import path
from . import views

app_name = 'hrm'

urlpatterns = [
    path('', views.index, name='index'),
    path('recruitment/', views.recruitment, name='recruitment'),
    path('department/', views.department, name='department'),
    path('employee-database/', views.employee_database, name='employee_database'),
    path('attendance/', views.attendance, name='attendance'),
    path('leave/', views.leave, name='leave'),
    path('payroll/', views.payroll, name='payroll'),
    path('reports/', views.reports, name='reports'),
]
