class Employee:
    def __init__(self, emp_id, name, desig, depart, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.designation = desig
        self.department = depart
        self.basic_salary = basic_salary
        self.hra_percentage = 20
        self.va_percentage = 30
        self.calculate_netsalary()

    def calculate_hra(self):
        return (self.basic_salary * self.hra_percentage) / 100

    def calculate_va(self):
        return (self.basic_salary * self.va_percentage) / 100

    def calculate_netsalary(self):
        hra = self.calculate_hra()
        va = self.calculate_va()
        self.hra = hra
        self.va = va
        self.netsalary = self.basic_salary + hra + va

    def display_employee_data(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Designation:", self.designation)
        print("Department:", self.department)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", self.hra)
        print("VA:", self.va)
        print("Net Salary:", self.netsalary)


emp1 = Employee(1, 'Vidit', 'Manager', 'Finance', 50000)
emp1.display_employee_data()
