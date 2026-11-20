class Employee():

    def __init__(self, name, idNumber, department, position):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        self.position = position

    def replace_employee(self, name, idNumber):
        self.name = name
        self.idNumber = idNumber
        self.department = ""
        self.position = ""
        
    def remove_employee(self):
        self.name = ""
        self.idNumber = 0
        self.departmemt = ""
        self.position = ""

    def change_id(self, name, idNumber):
        self.name = name
        self.idNumber = idNumber
    def change_position(self, department, position):
        self.department = department
        self.position = position

    def get_name(self):
        return self.name
    def get_idNumber(self):
        return self.idNumber
    def get_department(self):
        return self.department
    def get_position(self):
        return self.position

    def display_info(self):
        print("Name: " + self.name)
        print("ID number: " + str(self.idNumber))
        print("Department: " + self.department)
        print("Position: " + self.position)

class Janitor(Employee):

    #INHERITANCE
    def __init__(self, name, idNumber, department, position, shift):
        super().__init__(name, idNumber, department, position)
        self.shift = shift

    #NEW METHODS
    def get_shift(self):
        return self.shift
    def change_shift(self, shift):
        self.shift = shift

    #OVERRIDING
    def display_info(self):
        print("Name: " + self.name)
        print("ID number: " + str(self.idNumber))
        print("shift: " + self.shift)


def main():
    susan_meyers = Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
    mark_jones = Employee('Mark Jones', 39119, 'IT', 'Programmer')
    joy_rogers = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')

    print('EMPLOYEE:')
    susan_meyers.display_info()
    print()
    mark_jones.display_info()
    print()
    joy_rogers.display_info()
    print()

    bill_stevens = Janitor('Bill Stevens', 88803, None, None, '1st')
    jessie_hill = Janitor('Jessie Hill', 20353, None, None, '2nd')
    dennis_payne = Janitor('Dennis Payne', 22145, None, None, '3rd')

    print('JANITOR: ')
    bill_stevens.display_info()
    print()
    jessie_hill.display_info()
    print()
    dennis_payne.display_info()
    print()

    



main()
