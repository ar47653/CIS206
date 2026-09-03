"""
BMI = mass (kg) divided by height squared (m^2)
or lb/in^2 * 703
"""

def main():
    print("Enter your height in feet and inches: ")
    user_feet = int(input("feet: "))
    user_inches = int(input("inches: "))

    print("Enter you weight in pounds: ")
    user_pounds = float(input("weight(lbs): "))

    user_inches_total = (user_feet * 12) + user_inches
    user_BMI = (user_pounds / (user_inches_total ** 2)) * 703

    print("Your BMI is " + f"{user_BMI:.1f}")

    if user_BMI < 18.5:
        print("You are underweight.")
    elif user_BMI <= 18.5 and user_BMI <=25.0:
        print("You are in normal range.")
    elif user_BMI > 25.0 and user_BMI <= 30.0:
        print("You are overweight.")
    elif user_BMI > 30.0:
        print("You are obese.")

    print("source: https://en.wikipedia.org/wiki/Body_mass_index")


    






main()

