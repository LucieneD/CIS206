# BMI calulator 
"""
This program calculates the body mass index (BMI) based on the users weight and height. 
it will Classify the BMI into underweight, normal weight, overweight or obese
The user can also calculate multiple BMIs by choosing to continue 
"""

"""
prompts the user to enter a valid number (float)
"""
def get_number (prompt):
    while True:
        value = input (prompt)
        try:
            return float(value)
        except ValueError:
            print ("Invalid user input. Please enter valid number.")

def calculate_bmi(weight, height_ft, height_in):
    # convert height to total inches then to meters
    total_height_in = (height_ft*12) + height_in
    height_meters = total_height_in * 0.0254

    #convert weight to kilograms
    weight_kg = weight * 0.453592

    #calculate BMI
    bmi = weight_kg / (height_meters ** 2)
    #format BMI
    bmi_final = round(bmi, 1)

    print (f"Your BMI is: {bmi_final}")

    #classify BMI
    if bmi < 18.5:
        print ("Your BMI shows you are underweight.")
    elif 18.5 <= bmi <= 24.9:
        print ("Your BMI shows you are normal weight.")
    elif 25 <= bmi < 29.9:
        print("Your BMI shows you are overweight.")
    else:
        print("Your BMI shows you are obese.")

#Main loop
while True:
    #get user input
    weight = get_number ("Enter your weight in pounds: ")
    height_ft = int(get_number ("Enter your height in feet:"))
    height_in = int(get_number ("Enter your height in inches: "))

    calculate_bmi(weight, height_ft, height_in)

#ask user if they want to go again
    again = input ("Would you like to calculate another BMI? Please type Yes or No ") .strip().lower()
    if again != "yes":
        print ("Thank you for using the BMI calculator!")
        break



#Problem 4
