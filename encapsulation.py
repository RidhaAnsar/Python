class employee:
    def __init__(self, name, project, salary):
        self.name=name
        self.project=project
        self.salary=salary
    def show_info(self):
        print("Name:", self.name, "Salary:", self.salary, "Project:", self.project)
    def display(self):
        print(self.name, "is working on", self.project)
emp=employee("Ridha", "Data Analysis", 80000)

emp.show_info()
emp.display()
