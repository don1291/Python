#Basic Additions

a = 2
b = 3

total = a + b
print(total)


def addition(a,b):
    total = a + b
    print(total)
addition(5,3)

a = float(input("Enter the number:  "))
b = float(input("Enter the number:  "))
addition(a,b)

def subtraction(a,b):
    total = a - b
    print(total)
subtraction(a,b)


def multiplication(a,b):
    total = a * b
    print(total)
multiplication(a,b)


def division(a,b):
    total = a/b
    print(total)
division(a,b)

num1 = float(input("Enter the number:  "))
num2 = float(input("Enter the number:  "))

def find_max(num1,num2):
    if num1 > num2:
        print(num1)
    elif num1 == num2:
        print(num1)
    else:
        print(num2)
find_max(num1,num2)



num1 = float(input("Enter the Number:  "))
def feet_to_inches(num1):
    inches = num1 * 12
    return inches
print(num1)
feet_to_inches(num1)
