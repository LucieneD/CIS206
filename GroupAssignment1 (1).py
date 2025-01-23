

#Katsiaryna Fiodarava
#Luciene Doobay
#Nardeen Hameed
#Aryan Patel



# Applying coding standards:
# 1. Descriptive and meaningful function names
# 2. Proper indentation for readability
# 3. Consistent variable naming for clarity
# 4. Well-structured comments explaining each section of the program
# 5. Stick with 4 spaces per indentation level


def calculate_bmi(weight, height):
   #height of the individual in meters
   #weight of the individual in kilograms
   return weight / (height ** 2)


def calculate_bim_with_inches(weight, height_inches):
    height_meters = height_inches * 0.0254
    return calculate_bmi(weight, height_meters)


def determine_bmi_category(bmi):
   # Underweight (<18.5), Normal weight (18.5-24.9), Overweight (25-29.9), Obese (>=30)
   if bmi < 18.5:
       return "underweight"
   elif 18.5 <= bmi < 24.9:
       return "normal weight"
   elif 25 <= bmi < 29.9:
       return "overweight"
   else:
       return "obesity"
   

def main():

    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    height_inches = float(input("Enter your height in inches:"))
    bmi = calculate_bmi(weight, height) 
    bmi2 = calculate_bim_with_inches(weight, height_inches)
    category = determine_bmi_category(bmi)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"This is {category}")
  
main()


