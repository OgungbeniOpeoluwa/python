name = input("Enter Employee's name : ")
work_hour = int(input("Enter number of hours worked in a week: "))
hourly_pay_rate = float(input("Enter hourly pay rate: "))
month = input("Enter month: ")
federal_tax = int(input("Enter federal tax withholding rate: "))
state_tax = int(input("Enter federal tax withholding rate: "))


gross_pay = work_hour * hourly_pay_rate
federal_pay = (federal_tax / 100) * gross_pay
state_pay = (state_tax / 100) * gross_pay
total = federal_pay + state_pay
net_total = gross_pay - total
print()
print(f"""{name} payroll Statement for the month of {month}

Employee name : {name} 
name Hours worked : {work_hour}
pay rate: {hourly_pay_rate}
Gross pay : {gross_pay}

Deductions:
Federal WithHolding Rate : {federal_pay}
State Withholding: {state_pay}
Total Deduction:  {total}
Net Pay: {net_total} """)