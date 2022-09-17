print("BMI Calculator 2.0")
height = float(input("Height : "))
weight = float(input("Weight : "))
bmi = round(weight/height**2)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25.0:
    print("Normal Weight")
elif bmi <30:
    print("Overweight")
elif bmi < 35:
    print("Obese")
else:
    print("!! - BMI OUT OF RANGE!! ")
