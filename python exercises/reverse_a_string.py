#program to reverse a given string

#Take input from the user
text=input("Enter a string to reverse: ")

#Reverse the string using slicing
reversed_text=text[::-1]

#Display the result
print(f"The reversed string is: {reversed_text}")