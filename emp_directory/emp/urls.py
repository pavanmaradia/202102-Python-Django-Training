from django.urls import path

from emp.views import system_health, employee

urlpatterns = [
    path('system_health/', system_health),
    path('employee/', employee),
    path('employee/<str:emp_id>/', employee),
]
