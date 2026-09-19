"""
Name: Nori Honda
Assignment 4: Loops
"""



def define_user_inches():
    print("Enter your height in feet and inches. Enter 0 to quit.")

    #keep prompting until user enters valid data or enters 0 to quit
    user_feet = input("feet: ")
    while not user_feet.isnumeric() or int(user_feet) < 0:
        print("Please enter a valid number for feet and inches.")
        user_feet = input("feet: ")

    #this will trigger the program to quit in the main function
    if user_feet == "0":
        return 0

    #keep prompting until user enters valid data or enters 0 to quit
    user_inches = input("inches: ")
    while not user_inches.isnumeric() or int(user_inches) < 0:
        print("Please enter a valid number for feet and inches.")
        user_inches = input("inches: ")

    #this will trigger the program to quit in the main function
    if user_inches == "0":
        return 0

    user_total_inches = (int(user_feet) * 12) + int(user_inches)

    return (user_total_inches)


def define_user_pounds():
    print("Enter you weight in pounds. Enter 0 to quit.")

    #keep prompting until user enters valid data or enters 0 to quit
    user_pounds = input("weight(lbs): ")
    while not user_pounds.isnumeric() or int(user_pounds) < 0:
        print("Please enter a valid number for weight in pounds.")
        user_pounds = input("weight(lbs): ")

    #this will trigger the program to quit in the main function
    if user_pounds == "0":
        return 0

    return float(user_pounds)


def calculate_BMI(user_total_inches, user_pounds):
    user_BMI = (user_pounds / (user_total_inches ** 2)) * 703
    return user_BMI


def print_user_BMI(user_BMI):
    print("Your BMI is " + f"{user_BMI:.1f}")


def print_BMI_range(user_BMI):
    if user_BMI < 18.5:
        print("You are underweight.")
    elif user_BMI >= 18.5 and user_BMI <=25.0:
        print("You are in normal range.")
    elif user_BMI > 25.0 and user_BMI <= 30.0:
        print("You are overweight.")
    elif user_BMI > 30.0:
        print("You are obese.")

    print("source: https://en.wikipedia.org/wiki/Body_mass_index")

#this function will allow the user to restart or quit at the end of the program
def restart_prompt():
    Restart_prompt = input("type 1 to restart, 0 to quit: ")
    while not (Restart_prompt == "1") and not (Restart_prompt == "0"):
        print("Error: Please enter 1 or 0")
        Restart_prompt = input("type 1 to restart, 0 to quit: ")

    #this will trigger the program to restart in the main function
    if Restart_prompt == "1":
        return 1
    #this will trigger the program to quit in the main function
    elif Restart_prompt == "0":
        return 0

#This function creates a BMI table
def create_BMI_table():
    print("BMI Table: column:height (in) - row:weight (lbs)")
    height = []
    weight = []

    #list of height for columns
    for i in range(58, 77, 2):
        height.append(i)
    print("        ", end="")
    #list of weight for rows
    for i in range(100, 251, 10):
        weight.append(i)
        print(f"{i:4}\t",end="")
    print()

    #nested loop that use BMI formula to populate the table
    for row in height:
        print(f"{row:4}\t",end="")
        for col in weight:
            BMI = f"{(col / (row ** 2)) * 703:.2f}"
            print(f"{BMI:4}\t",end="")
        print()
 

def BMI_program():

    #define user's height in inches
    user_total_inches = define_user_inches()

    #quit program
    if user_total_inches == 0:
        return

    #define user's weight in pounds
    user_pounds = define_user_pounds()

    #quit program
    if user_pounds == 0:
        return

    #calculate user's BMI
    user_BMI = calculate_BMI(user_total_inches, user_pounds)
    print_user_BMI(user_BMI)

    #determine user's BMI category
    print_BMI_range(user_BMI)

    #BMI table is displayed
    create_BMI_table()

    #ask user to restart or quit
    restart = restart_prompt()
    return restart



def main():

    #while loop that restarts the program if the user wants to
    Continue = BMI_program()
    while Continue == 1:
        Continue = BMI_program()
    if Continue == 0:
        return

main()


        