# count how many vowels by using recursion 
def recVowelCount(word:str):
    word=word.lower()
    if not word:
        return 0
    count = 'aeiou'.count(word[0])
    return count + recVowelCount(word[1:])
print("number of vowels in - I love python -: ", recVowelCount("I love python"))

# using lambda and map 
number=[40,35, 10, 15, 20]
multipl= lambda num : num*num 
result=map(multipl,number )
print("result multyple [40,35, 10, 15, 20] is: ",list(result))
