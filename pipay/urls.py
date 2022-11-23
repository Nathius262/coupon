from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('dashboard', dashboard_view, name='dashboard'),
    path('task', task_view, name='task'),    
]