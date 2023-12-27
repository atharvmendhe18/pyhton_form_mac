class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name


class Developer(Employee):
    def __init__(self, emp_id, name, programming_language):
        super().__init__(emp_id, name)
        self.programming_language = programming_language


class Tester(Employee):
    def __init__(self, emp_id, name, testing_tool):
        super().__init__(emp_id, name)
        self.testing_tool = testing_tool


class Manager(Employee):
    def __init__(self, emp_id, name):
        super().__init__(emp_id, name)
        self.managed_employees = []

    def add_employee(self, employee):
        self.managed_employees.append(employee)

    def remove_employee(self, employee):
        self.managed_employees.remove(employee)

    def display_managed_employees(self):
        print("Employees managed by", self.name, ":")
        for employee in self.managed_employees:
            print(f"ID: {employee.emp_id}, Name: {employee.name}")


# Example usage:

# Create employees
dev1 = Developer(1, "John Doe", "Python")
tester1 = Tester(2, "Jane Doe", "Selenium")
manager1 = Manager(3, "Manager Smith")

# Add employees to the manager's list
manager1.add_employee(dev1)
manager1.add_employee(tester1)

# Display managed employees
manager1.display_managed_employees()

# Remove an employee from the manager's list
manager1.remove_employee(dev1)

# Display managed employees again
manager1.display_managed_employees()
