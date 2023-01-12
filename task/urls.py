from django.urls import path
from .views import *
app_name='task'
urlpatterns = [
path('',DoctorApi.as_view(),name='DoctorApi'),
path('addslots',DoctorApi.as_view(),name='addslots'),
]