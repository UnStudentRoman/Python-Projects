#BMI Index

print("This is a BMI calculator.")
weight = float(input("Please enter your weight(kg) :"))
height = float(input("Please enter your height(m) :"))

BMI = weight/(pow(height,2))
print("Your BMI is ", round(BMI,2))

if BMI < 18.5:
    print("You are underweight.")
elif BMI < 25:
    print("You have a normal weight.")
elif BMI < 30:
    print("You are overweight.")
elif BMI < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")