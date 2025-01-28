
# BMI Calculator with Validation, Exception Handling, and Nested If Statements

# Import for data validation (format validation example with regex)
import re

# Function to calculate BMI
def calculate_bmi(weight, height_ft, height_in):
    try:
        # Convert height to total inches, then to meters
        total_height_inches = (height_ft * 12) + height_in
        height_meters = total_height_inches * 0.0254

        # Convert weight to kilograms
        weight_kg = weight * 0.453592

        # Calculate BMI
        bmi = weight_kg / (height_meters ** 2)

        # Format BMI to one decimal place
        bmi_final = round(bmi, 1)

        print(f"Your BMI is: {bmi_final}")

        # Classify BMI (Nested if statement)
        if bmi < 18.5:
            print("Your BMI shows you are underweight.")
        elif 18.5 <= bmi <= 24.9:
            if bmi < 20:
                print("Your BMI shows you are normal weight, but closer to the underweight range.")
            else:
                print("Your BMI shows you are normal weight.")
        elif 25 <= bmi < 29.9:
            print("Your BMI shows you are overweight.")
        else:
            print("Your BMI shows you are obese.")

    except ZeroDivisionError:
        print("Height cannot be zero. Please enter a valid height.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main program
try:
    # Get user input with validation
    weight = input("Enter your weight in pounds: ")

    # Validation 1: Data type validation
    if not re.match(r"^\d+(\.\d+)?$", weight):
        raise ValueError("Weight must be a positive number.")
    weight = float(weight)

    # Validation 2: Range validation
    height_ft = int(input("Enter your height in feet (1-8): "))
    if height_ft < 1 or height_ft > 8:
        raise ValueError("Height in feet must be between 1 and 8.")

    height_in = int(input("Enter your height in inches (0-11): "))
    if height_in < 0 or height_in > 11:
        raise ValueError("Height in inches must be between 0 and 11.")

    # Call the BMI calculation function
    calculate_bmi(weight, height_ft, height_in)

# Exception handling for invalid input
except ValueError as ve:
    print(f"Input error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Thank you for using the BMI calculator!")

