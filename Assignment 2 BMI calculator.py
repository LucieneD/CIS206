#BMI calculator
#get user Input
weight = float(input( "Enter your weight in pounds: "))
height_ft = int(input( " Enter your Height in Feet: "))
height_in = int(input( "Enter your height in Inches:"))
def calculate_bmi(weight, height_ft, height_in):
    #convert height to total inches then to meters
    total_height_inches = (height_ft * 12) + height_in
    height_meters = total_height_inches * 0.0254

    #convert weight to Kilograms
    weight_kg = weight * 0.453592


    #calculate BMI
    bmi = weight_kg / (height_meters ** 2)

    #format BMI to one decimal place
    bmi_final= round (bmi,1)

    print(f"Your BMI is: {bmi_final}")

    #classifyBMI
    if bmi < 18.5:
        print("Your BMI shows you are underweight.")
    elif 18.5 <= bmi <=24.9:
        print ("Your BMI shows you are normal weight. ")
    elif 25 <= bmi < 29.9:
        print ("Your BMI shows you are overweight. ")
    else:
        print("Your BMI shows you are obese.")

calculate_bmi(weight, height_ft, height_in)
