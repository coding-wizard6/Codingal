h=float(input("Enter your height: "))
w=float(input("Enter you weight: "))

bmi=w/(h/100)**2
print("Your BMI is: ",bmi)

if bmi<=18.5:
    print("You are underweight")

elif bmi<=24.5:
    print("You are healthy")
    
elif bmi<=29.5:
    print("You are overweight")

elif bmi<=34.5:
    print("Severly overweight")

elif bmi<=39.5:
    print("You are obese")

else: 
    print("You are severely obese")

