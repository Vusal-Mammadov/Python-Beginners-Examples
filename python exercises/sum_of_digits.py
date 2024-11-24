#Program to sum the digits of a number

#Take input from the user
num=int(input("Enter a number: "))

#Initialize the sum to 0
digit_sum=0


#Loop to extract each digit and add it to the sum
while num>0:
    digit_sum+=num%10 #Add the last digit to the sum
    num=num//10 #Remove the last digit from the number

#print the result
print(f"The sum of digits is {digit_sum}")