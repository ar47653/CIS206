#import northwind data file and create list. close file.
def create_northwind_list(northwind_file):
    f = open(northwind_file, "r")
    northwind = f.readlines()
    f.close()
    for i in range(len(northwind)):
        northwind[i] = northwind[i].split('","')
        northwind[i] = [item.strip('"\n') for item in northwind[i]]
    return northwind

#function that sorts the data by company name
def sort_by_company(nlist):
    for company in nlist:
        list_item = []
        list_item.append(company[1])
        list_item.append(company[2])
        list_item.append(company[9])
        list_string = " - ".join(list_item)
        print(list_string)

#function that sorts the data by contact name
def sort_by_contact(nlist):
    contact_list = []
    for contact in nlist:
        list_item = []
        list_item.append(contact[2])
        list_item.append(contact[1])
        list_item.append(contact[9])
        contact_list.append(list_item)
    contact_list.sort()
    for contact in contact_list:
        contact_string = " | ".join(contact)
        print(contact_string)

#function that looks up data related to company name that the user enters
def search_by_company(nlist):
    company_input = input("Look up by company name: ")
    for item in nlist:
        if item[1].lower() == company_input.lower():
            company = " | ".join(item)
            print("")
            print(company)
            return
    print("company not found")
 
#function that looks up data related to contact name that the user enters
def search_by_contact(nlist):
    contact_input = input("Look up by contact name: ")
    for item in nlist:
        if item[2].lower() == contact_input.lower():
            contact = " | ".join(item)
            print("")
            print(contact)
            return
    print("contact not found")
    
#a menu of choices the user can choose from 
def menu(nlist):
    print("a - sort by company\nb - sort by contact\nc - search by company\nd - search by contact\ne - quit")
    user_input = input("Enter the letter for your choice: ")
    while user_input.lower() != "a" and user_input.lower() != "b" and user_input.lower() != "c" and user_input.lower() != "d" and user_input.lower() != "e":
        user_input = input("Error: doesn't match any letter of choice.\nEnter the letter for your choice: ")
    if user_input.lower() == "a":
        print("")
        sort_by_company(nlist)
    elif user_input.lower() == "b":
        print("")
        sort_by_contact(nlist)
    elif user_input.lower() == "c":
        search_by_company(nlist)
    elif user_input.lower() == "d":
        search_by_contact(nlist)
    elif user_input.lower() == "e":
        return 0
    

#main program that repeats until user decides to quit
def main():
    northwind_list = create_northwind_list("Northwind.txt")
    print("NORTHWIND DATA")
    menu(northwind_list)
    print("")
    while menu(northwind_list) != 0:
        print("")
        menu(northwind_list)
        print("")




main()





