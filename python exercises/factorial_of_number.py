#Program to calculate the factorial of a number

#Take input from the user 
num=int(input("Write a number: "))

#Initialize factorial variable
factorial=1

#Check if number is negative ,zero or positive
if num<0:
    print("Factorial does not exist for negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
    #Calculate factorial using a for loop
    for i in range(1,num+1):
        factorial*=i
    print(f"The factorial of {num} is {factorial}")