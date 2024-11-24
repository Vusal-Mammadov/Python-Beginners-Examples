#Program to check if a number is prime

#Take input from the user 
num=int(input("Enter a number to check if its prime: "))


#Prime number check
if num <= 1:
    print(f"{num} is not a prime number.") #Number less than or equal to 1 are not prime
else:
    is_prime=True
    for i in range(2,int(num**0.5)+1):  #Check divisors up to the square root of the number
        if num%i==0: #If divisible,its not prime
            is_prime=False
            break
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
