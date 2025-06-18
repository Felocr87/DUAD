#This module contains the data actions in the menu of options to do with the program "Proyecto_Estudiantes",
#   the options related to export and import csv data.

import csv



def write_csv_file(class_information, headers):

    if len(class_information) == 0:
        print ("""
        Error!!! There is not enough information.
        This option needs the information of at least one student. 
        """)

    else:
        print("""
        Type how you would like to name the file, followed by the file extension '.csv'
            Example: 
                    Name_of_the_file.csv
            (The default name is 'Students_Grades.csv')
            """)
        file_name_to_export = input("   Type the name: ")
        if len (file_name_to_export) == 0:
            file_name_to_export = "Students_Grades.csv"
        
        with open (file_name_to_export, "w", encoding="utf-8") as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(class_information)
        
        print(f"""
        The data was written on the file   {file_name_to_export}
                """)



def read_csv_file():
    while True:
        try:
            file_name_to_import = input("""
        Type the name of the csv file to import (include the file extension ".csv"), 
        or just press the 'enter' key to import the default file 'Students_Grades.csv'
            (The file must be in the same folder of this program)
            
        CSV file name:""")
            
            if len(file_name_to_import)==0:
                file_name_to_import = "Students_Grades.csv"

            with open(file_name_to_import, 'r',newline='',encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(row)
                break
        except:
            print(f"There is not a csv file named {file_name_to_import} on this folder")
    return (file_name_to_import)


def convert_csv_file_to_dictionary_list (file_path):
    class_information = []    
    
    headers_type = {
        "Full name":str,
        "Class":str,
        "Spanish grade":int,
        "English grade":int,
        "Social Studies grade":int,
        "Science grade":int,
        "Average grade":int,
    }
    
    with open(file_path, 'r',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_information = {key: headers_type[key](value) for key, value in row.items()}
            class_information.append(student_information)
        return (class_information)
    