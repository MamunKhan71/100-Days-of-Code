print("#########################")
print("Welcome to BMI CALCULATOR")
print("#########################")
height = input("Enter Your Height in M : ")
weight = input("Enter Your Weight in KG : ")
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)
