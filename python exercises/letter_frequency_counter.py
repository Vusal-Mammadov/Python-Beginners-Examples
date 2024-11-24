#Function to count letter frequency
def letter_frequency(text):
    #Remove spaces and convert to lowercase
    text=text.replace(" ","").lower()

    #Initialize an empty dictionary to store frequency
    frequency = {}

    for char in text:
        if char.isalpha(): #Consider only letters
            if char in frequency:
                frequency[char] +=1 #Increment count if letter exists
            else:
                frequency[char]=1  #Initialize count for new letter

    return frequency

#Input:Text from the user
text=input("Enter a string: ")

#Get the letter frequency
result=letter_frequency(text)

#Display the result
print("Letter frequencies:",result)