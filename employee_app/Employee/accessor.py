from employee_app.models import Employee



class EmployeeAccess:
    @staticmethod
    def get_all_employee():
        return Employee.objects.all().values()
    

    @staticmethod
    def get_employee_by_id(id):
        return Employee.objects.filter(id = id).first()
    
    @staticmethod
    def get_employee_by_name(name):
        return Employee.objects.filter(slug = name).all()
    

    @staticmethod
    def delete_employee(id):
        employee = EmployeeAccess.get_employee_by_id(id)
        employee.delete()

        