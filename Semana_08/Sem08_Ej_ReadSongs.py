def open_file_per_line_and_make_a_list (path):
    my_list = []
    with open(path) as file:
        for line in file.readlines():
            my_list.append (line.strip())
            print(f"Linea: {line.strip()}")
        return my_list



def write_a_file_from_a_list (some_list_to_write):
    with open("file_written_from_a_list.txt", "w") as file:
        for item in some_list_to_write:
            file.write(item + "\n")
        print ("The list was written in the file: file_written_from_a_list.txt")



def main():
    original_list = open_file_per_line_and_make_a_list ("list_of_songs.txt")
    new_list = sorted (original_list)
    print (new_list)
    write_a_file_from_a_list (new_list)




if __name__ == '__main__':
	main()



