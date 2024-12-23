def add(a,b):
    return a + b 

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divideby zero"
    return a/b


print(" welcome to  the simple calculator")
choice = int(input("enter your choice: "))
num1 = float(input("enter your first number: "))
num2 = float(input("Enter your second number: "))

if choice == 1: 
    print (f"the result is: {add(num1,num2)}")
elif choice == 2:
    print (f"the result is: {subtract(num1, num2)}")
elif choice == 3: 
    print (f"the result is: {multiply(num1, num2)}")
elif choice == 4: 
    print (f"teh result is: {divide(num1, num2)}")
else: 
    print("invalid choice. please try again.")
