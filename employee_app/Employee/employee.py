from .accessor import EmployeeAccess
import slugify

class Employee:
    @staticmethod
    def get_all_employee():
        datas = EmployeeAccess.get_all_employee()
        if datas == None:
            raise ValueError("No Data available")
        return datas
    
    @staticmethod
    def get_employee_by_id(id):
        data = EmployeeAccess.get_employee_by_id(id)
        if data:
            return data
        raise ValueError("No employee available")
    

    @staticmethod
    def get_employee_by_name(name):
        datas = EmployeeAccess.get_employee_by_name(name)
        if datas:
            return datas
        raise ValueError("No data available")
    

    @staticmethod
    def delete_employee(id):
        data = EmployeeAccess.get_employee_by_id(id)
        if not data:
            raise ValueError("Employee doesn't exists")
        EmployeeAccess.delete_employee(id)


    @staticmethod
    def add_slug(data):
        data["slug"] = slugify.slugify(data["name"])
        return data