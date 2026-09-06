"""
Name: Nori Honda
Naming convention: snake case and self defining
Use functions
Use notes explaining each function
"""



"""
name: define_user_inches
parameter: none
return: user_total_inches (float)
description: calculate user's height in inches
"""
def define_user_inches():
    print("Enter your height in feet and inches: ")
    user_feet = int(input("feet: "))
    user_inches = int(input("inches: "))
    user_total_inches = (user_feet * 12) + user_inches
    return user_total_inches

"""
name: define_user_pounds
parameter: none
return: user_pounds (float)
description: record user's weight in pounds
"""
def define_user_pounds():
    print("Enter you weight in pounds: ")
    user_pounds = float(input("weight(lbs): "))
    return user_pounds

"""
name: calculate_BMI
parameter: user_total_inches, user_pounds (floats)
return: user_BMI (float)
description: calculate user's BMI
"""
def calculate_BMI(user_total_inches, user_pounds):
    user_BMI = (user_pounds / (user_total_inches ** 2)) * 703
    return user_BMI

"""
name: print_user_BMI
parameter: user_BMI (float)
return: none
description: print user's BMI
"""
def print_user_BMI(user_BMI):
    print("Your BMI is " + f"{user_BMI:.1f}")

"""
name: print_BMI_range
parameter: user_BMI (float)
return: none
description: print which BMI range category the user falls into
"""
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


def main():
    #define user's height in inches
    user_total_inches = define_user_inches()

    #define user's weight in pounds
    user_pounds = define_user_pounds()

    #calculate user's BMI
    user_BMI = calculate_BMI(user_total_inches, user_pounds)
    print_user_BMI(user_BMI)

    #determine user's BMI category
    print_BMI_range(user_BMI)


main()

