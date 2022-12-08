class Main:
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

        def menu(menu):
            if menu == 1:
                menu_item = 1
            elif menu == 2:
                menu_item = 2
            else:
                menu_item = 3
            return menu_item

    while True:
        main_menu = int(input("""
    
Welcome to the Alberta Hospital (AH) Management system
Select from the following options, or select 0 to stop: 
1 - 	Doctors
2 - 	Facilities
3 - 	Laboratories
4 - 	Patients 
    
    """))
        if main_menu == 1:
            print("WORK IN PROGRESS")
        elif main_menu == 2:
            while True:
                menu = int(input("""
    Facilities Menu:
    1 - Display Facilities list
    2 - Add Facility
    3 - Back to the Main Menu

    """))
                if Facility.menu(menu) == 1:
                        menu_select = 1
                elif Facility.menu(menu) == 2:
                    menu_select = 2
                else:
                    menu_select = 3
                Facility.menu(menu)
                if menu_select == 1:
                    print(Facility.displayFacility())
                    print("back to previous menu")
                elif menu_select == 2:
                    name = input("Enter Facility Name: ")
                    Facility.addFacility(name)
                    print("back to previous menu")
                else: # menu == 3
                    break
        elif main_menu == 3:
            print("WORK IN PROGRESS")
        elif main_menu == 4:
            print("WORK IN PROGRESS")
        else: # main_menu == 0
            break