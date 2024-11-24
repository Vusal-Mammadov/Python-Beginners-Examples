#Program to print the multiplication table of a given number

#Take input from the user
num=int(input("Enter a number to display its multiplication table: "))

#Print the multiplication table
print(f"Multiplication table of{num}:")

for i in range(1,11): #Loop from 1 to 10 
    print(f"{num} x {i}={num*i}")