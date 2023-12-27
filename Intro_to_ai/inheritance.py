employees = []
developers = []
testers = []


class Employee:
    def __init__(self, name, id):
        self.ep_name = name
        self.id = id

    def name(self):
        return self.ep_name


class Develepor(Employee):
    def __init__(self, name, id):
        self.id = id
        print(f"ID of developer = {self.id}")


class Testers(Employee):
    def __init__(self, name, id):
        self.id = id
        print(f"ID of tester = {self.id}")


class Manager(Develepor, Testers):
    def __init__(self):
        pass
d1 = Develepor("atharv", 344)
print(d1.name())
