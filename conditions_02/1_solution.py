# show the age status getting user input

age = input("Enter your age :")
age_in_int = int(age)

if age_in_int < 12 :
    print("you are child")
elif age_in_int < 18 :
    print("you are teenager")
elif age_in_int >= 18 :
    print("you are adult")
