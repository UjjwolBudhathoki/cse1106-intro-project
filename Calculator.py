# This is a simple Calculator that can do basic calculations such as Add and subtract
print ("Welcome to My Calculator")

print("Please enter 1 for addition or enter 2 for subtraction\n")

user_choice = int(input("Enter choice number here: "))

user_input_num1 = int(input("Enter a first number here: "))
user_input_num2 = int(input("Enter a second number here: "))

result = 0

if user_choice == 1:
    result = user_input_num1 + user_input_num2
    print("The sum of two numbers is: ", result)

elif user_choice == 2:
    result = user_input_num1 -  user_input_num2
    print("The difference of two numbers is: ", result)

print("Thank you for using my calculator!")



