#FizzBuzz program:Print numbers from 1 to 100 with conditions

for num in range(1,101): #Loop from 1 to 100
    if num%3==0 and num%5==0: #Multiples of both 3 and 5
        print("FizzBuzz")
    elif num%3==0: #Multiples of 3 
        print("Fizz")
    elif num%5==0: #Multiples of 5
        print("Buzz")
    else:
        print(num)