from rest_framework.decorators import api_view
from employee_app.Employee.employee import Employee
from employee_app.api.response_builder import ResponseBuilder
from employee_app.api import api
from employee_app.Employee.serializers import EmployeeSerializer
from rest_framework.parsers import JSONParser

@api_view(["GET"])
def get_all_employee(request):
    response_builder = ResponseBuilder()
    try:
        data = Employee.get_all_employee()
        serializer = EmployeeSerializer(data, many  =True)
        return response_builder.get_200_ok_response(api.DATA_FETCHED, "List Of Employees", serializer.data)
    except ValueError as e:
        return response_builder.get_400_data_not_found_response(api.EMPLOYEE_NOT_FOUND, str(e))
    except Exception as e:
        return response_builder.get_500_server_error(api.SERVER_ERROR, str(e))
    




@api_view(["GET"])
def get_employee_by_id(request, id):
    response_builder = ResponseBuilder()
    try:
        data = Employee.get_employee_by_id(id)
        serializer = EmployeeSerializer(data)
        return response_builder.get_200_ok_response(api.DATA_FETCHED, "Employee data", serializer.data)
    except ValueError as e:
        return response_builder.get_400_bad_request(api.EMPLOYEE_NOT_FOUND, str(e))
    except Exception as e:
        return response_builder.get_500_server_error(api.SERVER_ERROR, str(e))
    

@api_view(["GET"])
def get_employee_by_name(request, name):
    response_builder = ResponseBuilder()
    try:
        data = Employee.get_employee_by_name(name)
        serializer = EmployeeSerializer(data, many = True)
        return response_builder.get_200_ok_response(api.DATA_FETCHED, "Employee data", serializer.data)
    except ValueError as e:
        return response_builder.get_400_bad_request(api.EMPLOYEE_NOT_FOUND, str(e))
    except Exception as e:
        return response_builder.get_500_server_error(api.SERVER_ERROR, str(e))
    


@api_view(["POST"])
def create_employee(request):
    response_builder = ResponseBuilder()
    try:
        data = JSONParser().parse(request)
        complete_data = Employee.add_slug(data)
        serializer = EmployeeSerializer(data= complete_data)
        if serializer.is_valid():
            serializer.save()
            return response_builder.get_201_data_created_response(api.DATA_CREATED, "Employee successfully added", serializer.data)
        return response_builder.get_400_bad_request(api.INVALID_INPUT, serializer.errors)
    except Exception as e:
        return response_builder.get_500_server_error(api.SERVER_ERROR, str(e))
    


@api_view(["PUT", "PATCH"])
def update_employee(request, id):
    response_builder = ResponseBuilder()
    try:
        data = JSONParser().parse(request)
        employee = Employee.get_employee_by_id(id)
        serializer = EmployeeSerializer(employee,data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return response_builder.get_201_data_created_response(api.DATA_CREATED, "Employee successfully added", serializer.data)
        return response_builder.get_400_bad_request(api.INVALID_INPUT, serializer.errors)
    except ValueError as e:
        return response_builder.get_400_bad_request(api.EMPLOYEE_NOT_FOUND, str(e))
    except Exception as e:
        return response_builder.get_500_server_error(api.SERVER_ERROR, str(e))
    

@api_view(["DELETE"])
def delete_employee(request, id):
    response_builder = ResponseBuilder()
    try:
        employee = Employee.get_employee_by_id(id)
        Employee.delete_employee(id)
        return response_builder.get_200_ok_response(api.DELETED_SUCCESS, "Deleted employee")
    except ValueError as e:
        return response_builder.get_400_bad_request(api.EMPLOYEE_NOT_FOUND, str(e))
    except Exception as e:
        return response_builder.get_500_server_error(api.SERVER_ERROR, str(e))
    