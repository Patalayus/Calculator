#Returns the sum of num1 and num2

def add(num1, num2):
    return num1 + num2
# * = multiplication

def multiply(num1, num2):
    return num1 * num2
# - = subtraction

def subtract(num1, num2):
    return num1 - num2
# / = division

def divide(num1, num2):
    return num1 / num2

def main():
    operation = input('What do you want to do?( +, -, *, /)')
    if (operation != '+' or operation != '-' or operation != '*' or operation != '/'):
        print('Please enter a valid integer')
    else:
        var1 = int(input('Enter num 1'))
        var2 = int(input('Enter num 2'))
        if operation == '+':
            print(add(var1, var1))
        elif operation == '-':
            print(divide(var1, var2))
        elif operation == '*':
            print(multiply(var1, var2))
        else:
            print(divide(var1, var2))


main()



























