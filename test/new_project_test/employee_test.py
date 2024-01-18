import unittest

from new_project.Invalid_work_hour_exception import InvalidWorkException
from new_project.employee import Employee


class MyTestCase(unittest.TestCase):
    def test_something(self):
        with self.assertRaises(InvalidWorkException):
            Employee.calculate_emp_salary(0)
        # self.assertEqual(200, numb)  # add assertion here

    def test_emp_assign_department(self):
        employee = Employee("123", "ope", "accounting")
        self.assertEqual("accounting", employee.get_emp_assign_department())

    def test_that_employee_can_print_details(self):
        employee = Employee("123", "ope", "accounting")
        employee_detail = employee.get_employee_details()
        print(employee_detail)


if __name__ == '__main__':
    unittest.main()
