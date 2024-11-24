#Program to generate the Fibonacci sequence up to a given number of terms

#Take input from the user
n_terms=int(input("Enter the number of terms for the Fibonacci sequence: "))

#Initialize the first two terms
a,b=0,1

#Validate input
if n_terms<=0:
    print("Please enter a positive integer.")
elif n_terms==1:
    print(f"Fibonacci sequence: {a}")
else:
    print("Fibonacci sequence:")
    for _ in range(n_terms):
        print(a,end=" ") #Print the current term
        a,b=b,a+b #Update to the next terms
