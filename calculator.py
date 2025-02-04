
#Function
def calculator():
     print("welcome to the simple calculator:")

#Taking operator
operator = input("enter an operator (+, -, *, /): ")

#Input from the user
num1 = float(input("enter the 1st number: "))

num2 = float(input("enter the 2nd number :"))

#Calculation
if operator == "+":
    result = num1 + num2
    print("The result of addition is: ", result)


elif operator == "-":
    result = num1 - num2
    print("The result of subtraction is: ", result)


elif operator == "*":
    result = num1*num2
    print("The result of multiplication is: ", result)


elif operator == "/":
    result = num1/num2
    if num2 != 0:
        print("the result is: ", result)
    else:
        print("division by zero!")
else:
    print("operator is not correct")

calculator()