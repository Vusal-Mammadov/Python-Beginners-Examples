#Program to calculate the area of a circle

#Import the math module to access pi
import math

#Take the input from the user 
radius=float(input("Enter the radius of the circle: "))

#Calculate the area using the formula:Area=pi*r^2
area=math.pi*(radius**2)

#Display the result
print(f"The area of the circle with radius {radius} is {area:.2f}")

