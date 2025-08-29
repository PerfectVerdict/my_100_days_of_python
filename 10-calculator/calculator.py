def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mult(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

dict = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}

on = True
num1 = int(input("Enter a number: "))
while on:
    user_operation = input("+ - * / : ")
    num2 = int(input("Enter a number: "))

    calculation_function = dict.get(user_operation)

    if calculation_function:
        result = calculation_function(num1, num2)
        print(f"The restult is {result}")
    else:
        print("Invalid operation")

    yes_or_no = input(f"Do you want to do another operation to {result}?: ")
    if yes_or_no == "yes":
        num1 = result
    else:
        on = False

