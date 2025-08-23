w = float(input("Enter your weight in KG"))
h = float(input("Enter your height in meter"))

bmi = w/h **2

print("Your BMI is:",round(bmi,2))

if bmi < 18.5:
    print("You are underweight. Please Some weight")
    
elif 18.5 <= bmi <= 24.9:
    print("you are normal in weight, keep it up")
    
elif 25 <= bmi <= 29.9:
    print("you are overweight, please loose some weight")
    
elif 30 <= bmi <= 34.9:
    print("you are obese, loosing weight is emergency")

else:
    print("You are extremly obese, please visit the doctor as soon as possible")