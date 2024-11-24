#Program to find the largest element in a list

#Take a list of numbers a input
numbers=list(map(int,input("Enter numbers separated by spaces: ").split()))

#Find the largest number 
largest=max(numbers)

#Dislay the result
print(f"The largest number in the list is: {largest}")