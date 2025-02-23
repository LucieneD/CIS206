
# BMI Calculator
"""
This program calculates the body mass index (BMI) based on the user's weight and height.
It classifies the BMI into underweight, normal weight, overweight, or obese.
"""

def get_number(prompt):
    """Prompts the user to enter a valid float number."""
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid user input. Please enter a valid number.")

def calculate_bmi(weight, height_ft, height_in):
    """
    Converts weight from pounds to kg, height from ft/in to meters,
    calculates BMI, and returns both the BMI and category.
    """
    # Convert height to total inches then to meters
    total_height_in = (height_ft * 12) + height_in
    height_meters = total_height_in * 0.0254

    # Convert weight to kilograms
    weight_kg = weight * 0.453592

    # Calculate BMI
    bmi = weight_kg / (height_meters ** 2)
    bmi_final = round(bmi, 1)

    # Classify BMI
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi_final, category  # Returns values instead of printing them

if __name__ == "__main__":
    # Main loop
    while True:
        # Get user input
        weight = get_number("Enter your weight in pounds: ")
        height_ft = int(get_number("Enter your height in feet: "))
        height_in = int(get_number("Enter your height in inches: "))

        # Calculate BMI
        bmi_value, bmi_category = calculate_bmi(weight, height_ft, height_in)
        print(f"Your BMI is: {bmi_value}")
        print(f"Your BMI shows you are {bmi_category}.")

        # Ask user if they want to go again
        again = input("Would you like to calculate another BMI? (Yes/No) ").strip().lower()
        if again != "yes":
            print("Thank you for using the BMI calculator!")
            break
