#This module contains the principal actions in the menu of options to do with the program "Proyecto_Estudiantes",
#   except the options related to export and import data.


import data


def ask_for_a_grade (subject):
    while True:
        try:
            grade_asked = int(input(f"   Type the {subject} grade (must be an integer from 0 to 100): "))
            if grade_asked >= 0 and grade_asked <=100:
                break
            else:
                print(f"  !!!  Invalid value. It must be an integer between 0 and 100. Type the {subject} grade again.")
        except:
            print(f"  !!!  Invalid value. It must be an integer between 0 and 100. Type the {subject} grade again.")
    return (grade_asked)



def ask_yes_or_not():
    while True:
        try:
            yes_or_not = int(input ("""
                        ( 1 ) Yes
                        ( 0 ) Not
                    Press your option number: """))
            if yes_or_not == 1 or yes_or_not == 0:
                break
            else:
                print("""
                Invalid value. You must type number 1 or number 0. Try again.""")
        except:
            print("""
                Invalid value. You must type number 1 or number 0. Try again.""")
    return (yes_or_not)



def ask_for_student_information():
    student_full_name = input ("   Full name: ")
    student_class = input ("   Class: ")
    spanish_grade = ask_for_a_grade("Spanish")
    english_grade = ask_for_a_grade("English")
    social_studies_grade = ask_for_a_grade("Social Studies")
    science_grade = ask_for_a_grade("Science")
    student_average = (spanish_grade + english_grade + social_studies_grade + science_grade) // 4
    
    student_information = {
        "Full name": student_full_name,
        "Class": student_class,
        "Spanish grade": spanish_grade,
        "English grade": english_grade,
        "Social Studies grade": social_studies_grade,
        "Science grade": science_grade,
        "Average grade": student_average,
        }
        
    return(student_information)



def make_class_information (class_information):
    student_info_is_right = 0
    print("""
            Type the information for each student
        """)
    
    while student_info_is_right == 0:
        student_information = ask_for_student_information()
        print ("""
        
                Please double check the given information about this student:
        """)
        print (student_information)

        print ("Is that information right?")
        student_info_is_right = ask_yes_or_not()
        if student_info_is_right == 0:
            print("""   
                Ok. Please type the information of this student again < < < """)
            
    class_information.append(student_information)
    print("""
            The information was added to the class information
            """)
    return(class_information)



def print_class_information(class_information):
    
    if len(class_information)== 0:
        print("There is not information yet")
    else:
        print (f"   The amount of provided students is: {len(class_information)}")
        print ("   This is the information of all the given students:")
        
        for student in class_information:
            print (student)
        


def give_the_top_3_students_average(class_information):
    
    sorted_class_information = sorted(class_information, key=lambda x: x["Average grade"], reverse=True)  #En esta línea me ayudé con chatgpt
    
    if len(class_information) < 3:
        print ("""
            Error!!! There is not enough information.
            This option needs the information of at least three students. 
            """)
    else:
        print ("    These are the three students with best average grades")
        index = 0
        while (index < 3):
            student_information = sorted_class_information[index]
            print(f"""
                Student N°{index+1}: 
                {student_information}""")
            index += 1
        
        print ("""
                    Congratulations!!!
            """)



def show_the_general_class_average_grade(class_information):

    if len(class_information) == 0:
        print ("""
            Error!!! There is not enough information.
            This option needs the information of at least one student 
            """)

    else:    
        sum_students_average = 0
        for student in class_information:
            sum_students_average += student["Average grade"]
            number_of_students = len(class_information)
        general_class_average = sum_students_average // number_of_students
        print (f"   The class average grade is: {general_class_average}")




