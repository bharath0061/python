val1 = input("Enter first value: ")
val2 = input("Enter second value: ")
print ("use corresponding Expression by for the operation\nAddition --> +\nSubstraction --> -\nMultiplication --> *\nDivision --> /\n")
val3 = input("Enter the expression: ")

user_input1 = int(val1)
user_input2 = int(val2)
user_input3 = val3

def simple_cal(user_input1, user_input2, user_input3):
#    add = "+"
#    sub = "-"
#    mul = "*"
#    div = "/"

    if user_input3 == "+":#add:
        print (f"Addition of given values is { user_input1 + user_input2 }")
    elif user_input3 == "-":#sub:
        print (f"Subtraction of given values is { user_input1 - user_input2 }")
    elif user_input3 == "*":#mul:
        print (f"Multiplication of given numbers is { user_input1 * user_input2 }")
    elif user_input3 == "/":#div:
        print (f"Division of given numbers is { user_input1 // user_input2}")
    else:
        print ("Invalid choice")

simple_cal(user_input1, user_input2, user_input3)
#print (simple_cal(user_input1, user_input2, user_input3))

