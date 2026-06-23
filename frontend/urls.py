from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/background/', views.about_background, name='about_background'),
    path('about/team/', views.about_team, name='about_team'),
    path('services/network-solution/', views.service_network, name='service_network'),
    path('services/cloud-solution/', views.service_cloud, name='service_cloud'),
    path('services/domain-hosting/', views.service_hosting, name='service_hosting'),
    path('services/managed-it/', views.service_managed_it, name='service_managed_it'),
    path('services/business-suite/', views.service_business_suite, name='service_business_suite'),
    path('courses/', views.training, name='training'),
    path('verify-certificate/', views.verify_certificate, name='verify_certificate'),
    path('courses/register/', views.register_course, name='register_course'),
    path('courses/inquire/', views.inquire_course, name='inquire_course'),
    path('contact/', views.contact, name='contact'),
]
