"""
BMI calculator with table
"""
def get_number (prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print ("Invalid user input. Please enter a valid number")

def calculate_bmi (weight, height_ft, height_in):
    #Convert height to total inches then to meters
    total_height_in = (height_ft *12) + height_in
    height_meters = total_height_in * 0.0254

    #convert weight to Kilos
    weight_kg = weight * 0.453592

    #calculate Bmi
    bmi = weight_kg / (height_meters ** 2)

    return round(bmi,1)
def bmi_table():
    """
    Heights: 58" - 76" (increments of 2)
    Weights: 100lbs - 250lbs (increments of 10)
    """
    print ("\nBMI Table")
    print ("Height |" + " ".join(f"{w}" for w in range (100,350, 10)))
    print ("-" * 80)

    for height_in in range (58,78,2):
        row = f"{height_in:>3} in |"
        for weight in range (100, 350, 10):
            bmi = calculate_bmi (weight, 0, height_in)
            row += f"{bmi:>5}"
        print (row)
while True:
    # Get user input
    weight = get_number("Enter your weight in pounds: ")  # Weight stays as float
    height_ft = int(get_number("Enter your height in feet: "))  # Convert to int
    height_in = int(get_number("Enter your height in inches: "))  # Convert to int

    # Calculate BMI
    bmi_result = calculate_bmi(weight, height_ft, height_in)
    print(f"\nYour BMI is: {bmi_result}")

    # Classify BMI
    if bmi_result < 18.5:
        print("Your BMI shows you are underweight.")
    elif 18.5 <= bmi_result <= 24.9:
        print("Your BMI shows you are normal weight.")
    elif 25 <= bmi_result < 29.9:
        print("Your BMI shows you are overweight.")
    else:
        print("Your BMI shows you are obese.")

    # Ask user if they want to see the BMI table
    show_table = input("Would you like to see the BMI table? (Yes/No): ").strip().lower()
    if show_table == "yes":
        bmi_table()

    # Ask user if they want to go again
    again = input("Would you like to calculate another BMI? Please type Yes or No: ").strip().lower()
    
    if again == "no":  # If user enters "No", exit the loop
        print("Thank you for using the BMI calculator!")
        break  # Exit the while loop