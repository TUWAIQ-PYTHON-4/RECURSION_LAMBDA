# Python3 program to count vowels
# in a string
 
# Function to check the Vowel
import re


def isVowel(check):
    return check.upper()  in ['A', 'E', 'I', 'O', 'U'] 

def isVowel2(check2):
    return check2.lower() in ['a','e','i','o','u']

# Returns count of vowels in str
def countVowels(str):
    count = 0
    for i in range(len(str)):
 
        # Check for vowel
        if isVowel(str[i]):
         
            count += 1
        elif isVowel2(str[i]):
            count += 1
    print("total vowels number is: ")
    return count

str = input("write :")
print(countVowels(str))
print("____________Q2_____________")
result=list(map(lambda n: n * n, [40, 35, 10, 15, 20]))
print(result)