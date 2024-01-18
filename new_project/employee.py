from new_project.Invalid_work_hour_exception import InvalidWorkException


class Employee:
    hourly_rate = 10

    def __init__(self, emp_id, emp_name, emp_department):
        self._emp_ide = emp_id
        self._emp_name = emp_name
        self._emp_department = emp_department

    def set_name(self, name):
        self._emp_name = name

    def get_name(self):
        return self._emp_name

    def set_id(self, emp_id):
        self._emp_ide = emp_id

    def get_id(self):
        return self._emp_ide

    def get_emp_assign_department(self):
        return self._emp_department

    def set_emp_assign_department(self, department):
        self._emp_department = department

    def get_employee_details(self):
        return f"""
        EMPLOYEE DETAILS
        emp_id: {self._emp_ide},
        emp_name: {self._emp_name},
        emp_department: {self._emp_department},
        emp_hourly_rate: {Employee.hourly_rate}"""

    @staticmethod
    def calculate_emp_salary(number_of_work):
        if number_of_work < 1:
            raise InvalidWorkException()
        return number_of_work * Employee.hourly_rate

