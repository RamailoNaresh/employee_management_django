from django.urls import path
from employee_app.Employee import views as employee_views

urlpatterns = [
    path("employees/", employee_views.get_all_employee, name = "employees"),
    path("employee/<str:id>/", employee_views.get_employee_by_id, name = "employee-by-id"),
    path("employee_by_name/<str:name>/", employee_views.get_employee_by_name, name = 'employee-by-name'),
    path("create_employee/", employee_views.create_employee, name = "create-employee"),
    path("update_employee/<str:id>/", employee_views.update_employee, name = "update-employee"),
    path("delete_employee/<str:id>/", employee_views.delete_employee, name = "delete-employee")
]
