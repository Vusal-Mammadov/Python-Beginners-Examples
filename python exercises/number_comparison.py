#Program to compare two numbers and print the larger one

#Take input from the user 
num1=int(input("Write first number: "))
num2=int(input("Write second number: "))

#Compare the two numbers
if num1>num2:
    print(f"{num1} is larger than {num2}")
elif num2>num1:
    print(f"{num2} is larger than {num1}")
else:
    print(f"{num1} and {num2} are equal numbers.")