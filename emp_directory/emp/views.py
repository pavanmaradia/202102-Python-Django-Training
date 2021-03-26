import json

from django.http import JsonResponse
from django.shortcuts import render

from emp.models import Employee, City, State, Country


# Create your views here.


def system_health(request):
    return JsonResponse({'status': 'EMP System is up and running.'},
                        safe=False)


def employee(request, emp_id=None):
    if request.method == 'GET':
        if emp_id == None:
            response = employee_list(request)
        else:
            response = employee_get(emp_id)
    elif request.method == 'POST':
        response = employee_create(request)

    return response


def employee_get(emp_id):
    """
    Get employee from requested id
    :param request:
    :return:
    """
    try:
        emp = Employee.objects.get(id=emp_id)
    except Employee.DoesNotExist:
        return JsonResponse({
            'status': False,
            'message': 'Employee does not exists in database'
        }, status=404)
    _data = {
        'id': emp.id,
        'first_name': emp.first_name,
        'last_name': emp.last_name,
        'age': emp.age,
        'city': emp.city.name,
        'state': emp.state.name,
        'country': emp.country.name
    }
    return JsonResponse(_data, safe=False)


def employee_list(request):
    """ return list of employees """
    response_data = []
    for emp in Employee.objects.all().values(
            'id', 'first_name', 'last_name', 'age', 'address', 'city',
            'state', 'country'):
        response_data.append(emp)
    return JsonResponse(response_data, safe=False)


def employee_create(request):
    """
    Create Employee
    :param request:
    :return:
    """
    payload = json.loads(request.body.decode('utf-8'))

    try:
        city = City.objects.get(id=payload.get('city'))
    except City.DoesNotExist:
        return JsonResponse({
            'status': False,
            'message': 'Mention city does not exists in database'
        }, status=404)

    payload['city'] = city

    try:
        state = State.objects.get(id=payload.get('state'))
    except State.DoesNotExist:
        return JsonResponse({
            'status': False,
            'message': 'Mention state does not exists in database'
        }, status=404)

    payload['state'] = state

    try:
        country = Country.objects.get(id=payload.get('country'))
    except Country.DoesNotExist:
        return JsonResponse({
            'status': False,
            'message': 'Mention Country does not exists in database'
        }, status=404)

    payload['country'] = country

    emp = Employee.objects.create(**payload)
    return JsonResponse({'status': True})


def home(request):
    return render(request, 'home.html')


def employee_create_page(request):
    return render(request, 'employee_create.html')


def employee_list_page(request):
    response_data = []
    for emp in Employee.objects.all():
        _emp = {
            'id': str(emp.id),
            'first_name': emp.first_name,
            'last_name': emp.last_name,
            'age': emp.age,
            'city': emp.city.name,
            'state': emp.state.name,
            'country': emp.country.name
        }
        response_data.append(_emp)
    return render(request, 'employee_list.html', {'employee': response_data})
