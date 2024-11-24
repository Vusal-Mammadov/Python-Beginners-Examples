#Program to check if a string is a palindrome

#Take input from the user
text=input("Enter a string to check if its a palindrome: ").lower()   #Convert to lowercase for uniformity

#Remove spaces and special characters
cleaned_text=''.join(char for char in text if char.isalnum())

#Check if the cleaned string is equal to its reverse
if cleaned_text==cleaned_text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
