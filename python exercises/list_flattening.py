#Function to flatten a nested list
def flatten_list(nested_list):
    flat_list=[] #Initialize an empty list
    for item in nested_list:
        if isinstance(item,list): #Check if the item is a list
            flat_list.extend(flatten_list(item)) #Recursively flatten the list
        else:
            flat_list.append(item) #Append non list items directly
    return flat_list


#Input:Nested list
nested_list=[[1,2],[3,4,[5,6]],7]

#Flatten the list
result=flatten_list(nested_list)

#Output the result
print("Flattened List:",result)