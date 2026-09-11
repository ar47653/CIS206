"""
Assignment 3
"""

def main():

    try: 
        print("Enter your height in feet and inches: ")
        user_feet = int(input("feet: "))
       
        #CONSTRAINT VALIDATION
        user_inches = int(input("inches: "))
        while user_inches < 0 or user_inches > 12:
            print("Must be between 0 and 12!")
            user_inches = int(input("inches: "))
    
        print("Enter you weight in pounds: ")
        user_pounds = float(input("weight(lbs): "))

    #DATA TYPE VALIDATION
    except ValueError as e:
        print("please enter a number!", e)

    else:
        user_inches_total = (user_feet * 12) + user_inches
        user_BMI = (user_pounds / (user_inches_total ** 2)) * 703

        print("Your BMI is " + f"{user_BMI:.1f}")

        #NESTED IF STATEMENTS
        if user_BMI < 18.5:
            print("You are underweight.")
            if user_BMI < 16:
                print("Notice: This is severe thinness, please consult a doctor")
        elif user_BMI <= 18.5 and user_BMI <=25.0:
            print("You are in normal range.")
        elif user_BMI > 25.0 and user_BMI <= 30.0:
            print("You are overweight.")
        elif user_BMI > 30.0:
            print("You are obese.")
            if user_BMI > 40:
                print("Notice: This is class 3 obesity, please consult a doctor")

        print("source: https://en.wikipedia.org/wiki/Body_mass_index")


    






main()
