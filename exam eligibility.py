reason = input("Do you have medical reason: (yes/no): ").lower()

if reason == "yes":
    attendence = int(input("Enter your attendence percentage: "))
    if attendence >= 60:
        print("You are eligible for exam.")
    else:
        print("You are not eligible for exam.")
elif reason == "no":
    attendence = int(input("Enter your attendence percentage: "))
    if attendence >= 75:
        print("You are eligible for exam.")
    else:
        print("You are not eligible for exam.")
else:
    print("Invalid input! Please choose from yes or no.")