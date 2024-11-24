#Function to find unique elements in a list
def find_unique_elements(input_list):
    #Create an empty dictionary to store frequencies
    frequency={}

    #Count the occurences of each element
    for item in input_list:
        if item in frequency:
            frequency[item]+=1
        else:
            frequency[item]=1

    #Find elements with frequency 1 (unique elements)
    unique_elements=[key for key,value in frequency.items() if value==1]

    return unique_elements

#Input:List from the user
user_input=input("Enter numbers separated by spaces: ")
input_list=list(map(int,user_input.split()))

#Find unique elements 
result=find_unique_elements(input_list)

#Output the result
print("Unique elements:",result)