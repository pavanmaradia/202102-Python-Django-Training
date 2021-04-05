from django.urls import path

from emp.views import system_health, employee, home, employee_list_page, \
    employee_create_page, employee_form_view, create_bank_details

urlpatterns = [
    path('system_health/', system_health),
    path('employee/', employee),
    path('emp_form_view/', employee_form_view),
    path('bank_details/', create_bank_details),
    path('employee/<str:emp_id>/', employee),
    path('home', home),
    path('emp_page/', employee_list_page),
    path('emp_create_page/', employee_create_page)
]
