class Payroll:

    def __init__(self, employee_name = []):
        self.employee_name = employee_name

    def add(self, employee):
        self.employee_name.append(employee)

    def print(self):

        for e in self.employee_name:
            print(f"{e.full_name} INR. {e.get_salary()}")
    

