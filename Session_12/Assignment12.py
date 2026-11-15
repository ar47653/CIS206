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


class Patient():

    def __init__(self, name, address, phoneNumber, emergencyContact):
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber
        self.emergencyContact = emergencyContact

    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    def get_phoneNumber(self):
        return self.phoneNumber
    def get_emergencyContact(self):
        return self.emergencyContact

    def change_name(self, name):
        self.name = name
    def change_address(self, address):
        self.address = address
    def change_phoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber
    def change_emergencyContact(self, emergencyContact):
        self.emergencyContact = emergencyContact

    def display_info(self):
        print(f"name: {self.name}")
        print(f"address: {self.address}")
        print(f"phone number: {self.phoneNumber}")
        print(f"emergency contact: {self.emergencyContact}")


class Procedure():

    def __init__(self, name, date, practitioner, charge):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charge = charge

    def get_name(self):
        return self.name 
    def get_date(self):
        return self.date 
    def get_practitioner(self):
        return self.practitioner
    def get_charge(self):
        return self.charge

    def change_name(self, name):
        self.name = name 
    def change_date(self, date):
        self.date
    def change_practitioner(self, practitioner):
        self.practitioner
    def change_charge(self, charge):
        self.charge

    def display_info(self):
        print(f"name: {self.name}")
        print(f"date: {self.date}")
        print(f"practitioner: {self.practitioner}")
        print(f"charge: {self.charge}")


 
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

    print()
    print('PATIENT:')
    patient_1 = Patient('Tyler D. Johnson', '2532 Walnut ln. Chicago IL, 60003', '253-555-2534', 'Pam Johnson 462-555-3958')
    patient_1.display_info()
    print()

    print('PROCEDURE:')
    procedure_1 = Procedure('Physical Exam', '11/12/2026', 'Dr. Irvine', '$250.00')
    procedure_1.display_info()
    print()
    procedure_2 = Procedure('X-ray', '11/20/2026', 'Dr. Jamison', '$500.00')
    procedure_2.display_info()
    print()
    procedure_3 = Procedure('Blood test', '12/12/2026', 'Dr. Smith', '$200.00')
    procedure_3.display_info()
    print()


main()

