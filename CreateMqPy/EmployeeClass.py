import json

# Define the Employee class
class Employee:
    def __init__(self, id, name, age, salary, designation, department_name):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary
        self.designation = designation
        self.department_name = department_name

    def to_json(self):
        return json.dumps(self.__dict__)
