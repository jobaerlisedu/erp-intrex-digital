from django.urls import path
from . import views

app_name = 'solutions'

urlpatterns = [
    path('', views.index, name='index'),
]
