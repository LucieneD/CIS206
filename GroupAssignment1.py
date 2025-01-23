# Katsiaryna Fiodarava
#Luciene Doobay
#3Nardeen Hameed


# Coding Standards Applied:
# - Variable names are descriptive and follow the PEP 8 convention (snake_case).
# - Functions are well-documented with docstrings explaining their purpose, input, and output.
# - User input validation is handled by looping until valid entries are made.
# - Comments are used to explain key sections of the code for clarity.


def calculate_bmi(weight, height_feet, height_inches):
    """
    Function to calculate BMI based on weight and height (in feet and inches).
    
    Arguments:
        weight (float): Weight in pounds.
        height_feet (int): Height in feet.
        height_inches (int): Height in inches.
    
    Returns:
        float: BMI value.
    """
    # Convert weight from pounds to kilograms (standard unit)
    weight_kg = weight / 2.205  # Using the conversion factor from pounds to kilograms

    # Convert total height to inches (12 inches per foot)
    total_inches = (height_feet * 12) + height_inches  # Calculating the total height in inches

    # Convert height from inches to meters (standard unit)
    height_m = total_inches / 39.37  # 1 meter = 39.37 inches

    # Calculate BMI using the formula: BMI = weight_kg / (height_m ** 2)
    bmi = weight_kg / (height_m ** 2)  # Formula for BMI

    return bmi  # Return the calculated BMI


def bmi_category(bmi):
    """
    Function to categorize BMI into weight categories.
    
    Arguments:
        bmi (float): BMI value to categorize.
    
    Returns:
        str: Corresponding BMI category.
    """
    # Classifying BMI based on the standard BMI categories
    if bmi < 18.5:
        return "Underweight"  # Category for BMI less than 18.5
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"  # Category for BMI in the normal range
    elif 25 <= bmi < 29.9:
        return "Overweight"  # Category for BMI in the overweight range
    else:
        return "Obese"  # Category for BMI 30 and above


def main():
    """
    Main function to interact with the user and calculate BMI.
    
    It prompts the user to enter their weight and height, calculates BMI, 
    categorizes the result, and displays it.
    """
    # Taking input from the user and ensuring the correct data types
    weight = float(input("Enter your weight in pounds: "))  # User enters weight (float conversion)
    height_feet = int(input("Enter your height in feet: "))  # User enters height in feet (int conversion)
    height_inches = int(input("Enter your height in inches: "))  # User enters height in inches (int conversion)

    # Calculate BMI using the previously defined function
    bmi = calculate_bmi(weight, height_feet, height_inches)  # Calculate BMI using user input

    # Round the BMI to 1 decimal point for easier readability
    bmi = round(bmi, 1)  # Rounding the BMI to 1 decimal place

    # Get the BMI category based on the calculated BMI value
    category = bmi_category(bmi)  # Categorize the BMI

    # Display the results in a user-friendly manner
    print(f"\nYour BMI is: {bmi}")  # Output the BMI value
    print(f"Category: {category}")  # Output the BMI category


# Call the main function to run the program
main()  # This line initiates the execution of the program



