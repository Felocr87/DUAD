#This module contains the menu of options to do with the program "Proyecto_Estudiantes"

import data

import actions



def give_the_option_menu ():
    while True:
        try:
            print ("""
            These are the program options:
                1 Type student's information
                2 Look at the information of all students
                3 Look at the top 3 student's average grade 
                4 Look at the class average grade
                5 Export all the data to a .CSV document
                6 Import data from a .CSV existing document
                7 Exit
                
            What would you like to do?
                """)
            
            option_number = int(input("   Type the number of the option you'd like to do: "))
            
            my_options_list = [
                "Type student's information",
                "Look at the information of all the students",
                "Look at the top 3 student's average grade",
                "Look at the class average grade",
                "Export all the data to a .CSV document",
                "Import data from a .CSV existing document",
                "Exit",
                ]
            
            if option_number >= 1  and option_number <= 7 :
                print (f"""
                    Your option number is {option_number}: {my_options_list[option_number - 1]}""")
                
            else:
                raise ValueError()
            
            return (option_number)

        except:
            print("  !!!   Invalid value option. Try again! (Remember typing an integer number according to the menu options)")



def run_the_program_options ():

    class_information = []

    information_headers = [
        "Full name",
        "Class",
        "Spanish grade",
        "English grade",
        "Social Studies grade",
        "Science grade",
        "Average grade"
    ]

    while True:
        
        option_number = give_the_option_menu()

        if option_number == 1:
            class_previous_information = class_information
            class_information = actions.make_class_information(class_previous_information)

        elif option_number == 2:
            actions.print_class_information(class_information)
        
        elif option_number == 3:
            actions.give_the_top_3_students_average(class_information)
        
        elif option_number == 4:
            actions.show_the_general_class_average_grade(class_information)
        
        elif option_number == 5:
            data.write_csv_file(class_information, information_headers)
            
        elif option_number == 6:
            
            file_name_to_import = data.read_csv_file()

            print (""""
                Do you want to continue working on this information?""")
            use_data_from_csv = actions.ask_yes_or_not()
            if use_data_from_csv == 1:
                class_information = data.convert_csv_file_to_dictionary_list(file_name_to_import)
                print(f"""
                The information of the students is:
                    {class_information}
                    """)
                print (f"The information was loaded from file {file_name_to_import}")
            else:
                print (f"The information from file {file_name_to_import} was not loaded to this program")
            
        elif option_number == 7:
            print("""
                Thanks for using this program! Come back soon!
                
                """)
            break

        input("Press the key 'Enter' to continue...")