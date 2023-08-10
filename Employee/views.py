from django.shortcuts import render
from Employee.serializers import DepartmentSerializer,EmployeeSerializer
from Employee.models import Department,Employee
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# Create your views here.
@csrf_exempt

def DepartmentApi(request, id = 0):
    if request.method == "GET":
        departments = Department.objects.all()
        departments_serializers = DepartmentSerializer(departments,many = True)
        return JsonResponse(departments_serializers.data,safe=False)
    elif request.method == "POST":
        departments_data = JSONParser().parse(request)
        departments_serializers = DepartmentSerializer(data=departments_data)
        if departments_serializers.is_valid():   
            departments_serializers.save()
            return JsonResponse("Added Successfully!",safe=False)
        return JsonResponse("Failed!",safe=False)
    elif request.method == "PUT":
        departments_data = JSONParser().parse(request)
        department = Department.objects.get(id=departments_data["id"])
        departments_serializers = DepartmentSerializer(department,data=departments_data)
        if departments_serializers.is_valid():   
            departments_serializers.save()
            return JsonResponse("Updated Successfully!",safe=False)
        return JsonResponse("Failed Updating!",safe=False)
    elif request.method == "DELETE":
        department_data = JSONParser().parse(request)
        department = Department.objects.get(id=department_data["id"])
        department.delete()
        return JsonResponse("Deleted Successfully!",safe=False)
    
@csrf_exempt
    
def EmployeeApi(request, id = 0):
    if request.method == "GET":
        employess = Employee.objects.all()
        employees_serializers = EmployeeSerializer(employess,many = True)
        return JsonResponse(employees_serializers.data,safe=False)
    elif request.method == "POST":
        employees_data = JSONParser().parse(request)
        employess_serializers = EmployeeSerializer(data=employees_data)
        if employess_serializers.is_valid():   
            employess_serializers.save()
            return JsonResponse("Added Successfully!",safe=False)
        return JsonResponse("Failed!",safe=False)
    elif request.method == "PUT":
        employees_data = JSONParser().parse(request)
        employee = Employee.objects.get(id=employees_data["id"])
        employees_serializers = EmployeeSerializer(employee,data=employees_data)
        if employees_serializers.is_valid():   
            employees_serializers.save()
            return JsonResponse("Updated Successfully!",safe=False)
        return JsonResponse("Failed Updating!",safe=False)
    elif request.method == "DELETE":
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(id=employee_data["id"])
        employee.delete()
        return JsonResponse("Deleted Successfully!",safe=False)
    
        

