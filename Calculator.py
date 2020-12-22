num1 = float(input("enter a number:"))
Calculation = ("Multiply", "Divide", "Add", "Subtract")
print(Calculation)
question = input("What calculation do you want to perform:")
num2 = float(input("enter a second number:"))


if question == "Multiply" or question == "multiply" or question == "*":
    print(num1 * num2)
elif question == "Divide" or question == "divide" or question == "/":
    print(num1 / num2)
elif question == "Add" or question == "add" or question == "+":
    print(num1 + num2)
elif question == "Subtract" or question == "subtract" or question == "-":
    print(num1 - num2)
else:
    print("Please enter an operator")


