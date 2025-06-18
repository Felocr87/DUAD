#This is the main module of the project at 10th week. This program makes and analyzes a data base of student's grades, and it needs to import
#  the external modules "menu", "actions" and "data" for using correctly. 


import menu



def main ():
    print ("Hello! This program makes and analyzes a data base of student's grades given by the user")
    try:
        menu.run_the_program_options ()

    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")



if __name__ == "__main__":
    main()