from django.shortcuts import render
# from django.http import Http404
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Employee
# Create your views here.
def employee_detail(request, pk):
    # try:
    #     employee = Employee.objects.get(pk = pk)
    #     print(employee)
    # except:
    #     raise Http404
    # Above methond is longcut method to handle 404 error
    employee = get_object_or_404(Employee, pk=pk)
    # return HttpResponse(f"{employee.first_name} {employee.last_name}") not better way to print it
    context = {
        'employee': employee,
    }  
    return render(request, 'employee_details.html', context)
