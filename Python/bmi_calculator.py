height = float(input("Enter your height (cm): "))
weight = float(input("Enter your weight (kg): "))
 
height = height/100
BMI = weight/(height*height)

print("Your Body Mass Index (BMI) value : ", BMI)

if BMI > 0:
    if BMI <= 16:
        print("Category - Severe Underweight")
    elif BMI <= 18.5:
        print("Category - Underweight")
    elif BMI <= 25:
        print("Category - Healthy")
    elif BMI <= 30:
        print("Category - Overweight")
    else: 
        print("Category - Severe Overweight")
else:
    ("Enter valid details")
