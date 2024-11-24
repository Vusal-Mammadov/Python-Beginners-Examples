#Function to check if two strings are anagrams

def are_anagrams(str1,str2):
    #Remove spaces and convert to lowercase for accurate comparison
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()

    #Check if sorted characters of both strings are equal
    return sorted(str1)==sorted(str2)

#Input:Two strings
string1=input("Enter the first string: ")
string2=input("Enter the second string: ")

#Check if the strings are anagrams
if are_anagrams(string1,string2):
    print(f"{string1} and {string2} are anagrams")
else:
    print(f"{string1} and {string2} are not anagrams.")