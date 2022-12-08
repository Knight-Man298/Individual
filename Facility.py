class Facility:
    def addFacility(name):
        facility_file = open("OOP1/Classes and Objects/files/facilities.txt", "a")
        with facility_file as file_object:
            file_object.write(f"\n{name}")
        return facility_file

    def displayFacility():
        facility_file = open("OOP1/Classes and Objects/files/facilities.txt","r")
        contents = facility_file.read()
        return contents

    def menu():
        menu = """"Facilities Menu:
1 - Display Facilities list
2 - Add Facility
3 - Back to the Main Menu"""
        return menu
