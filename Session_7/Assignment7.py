#open the provided names.txt file, create a list of names from it, then close file
def list_creation(textfile):
    text_file = open(textfile, "r")
    file_list = []
    for line in text_file:
        name = text_file.readline()
        name = name.replace("\n", "")
        file_list.append(name)
    text_file.close()
    return file_list

#user to input names. Names not in the list will be added to a new list of names.
def user_name_input(namelist):
    new_names = []
    user_name = input("Enter a name (type 'exit' to quit): ")
    while user_name not in namelist and user_name != "exit":
        new_names.append(user_name)
        print(user_name + " is added to new names list.")
        user_name = input("Enter another name (type 'exit' to quit): ")
        while user_name in namelist or user_name in new_names:
            print("This name is already in the list or new list")
            user_name = input("Enter another name (type 'exit' to quit): ")
    if user_name == "exit":
        return new_names

#output the list new names to a new text file called new_name_list.txt
def output_new_names(newnamelist):
    output_file = open("new_name_list", "w")
    for name in newnamelist:
        output_file.write(str(name) + "\n")
    print("new name list written to new_name_list.txt")
    output_file.close()




def main():
    name_list = list_creation("names.txt")
    new_names = user_name_input(name_list)
    output_new_names(new_names)

    

main()


