class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f"Name: {self.name}, ID: {self.id}"

class Manager(Employee):
    def __init__(self, name, id, department, project):
        super().__init__(name, id)
        self.department = department
        self.project = project

    def manage_project(self):
        return f"Manager {self.name} is working on a project {self.project}."

class Technician(Employee):
    def __init__(self, name, id, specialization, TS):
        super().__init__(name, id)
        self.specialization = specialization
        self.TS = TS

    def perform_maintenance(self):
        return f"Technician {self.name} is repairing {self.TS}."

class TechManager(Employee):
    def __init__(self, name, id, department, project, specialization, TS):
        # Вызов конструкторов вручную
        Employee.__init__(self, name, id)
        self.department = department
        self.project = project
        self.specialization = specialization
        self.TS = TS
        self.employees = []

    def manage_project(self):
        return f"Manager {self.name} is working on a project {self.project}."

    def perform_maintenance(self):
        return f"Technician {self.name} is repairing {self.TS}."

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_team_info(self):
        team_info = [employee.get_info() for employee in self.employees]
        return "\n".join(team_info)

# Создание объектов
employee = Employee("Avzad", 1)
manager = Manager("Mustafa", 2, "Games", "Half-Life 3")
technician = Technician("Shahzadbeck", 3, "Network Security", "user password security")
tech_manager = TechManager("Abdurahamzat", 4, "Development", "Optimization", "Software", "Fixing bugs")

# Добавление сотрудников в команду тех. менеджера
tech_manager.add_employee(employee)
tech_manager.add_employee(manager)
tech_manager.add_employee(technician)

# Вывод информации
print(employee.get_info())
print(manager.manage_project())
print(technician.perform_maintenance())
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance())
print("Team Info:")
print(tech_manager.get_team_info())