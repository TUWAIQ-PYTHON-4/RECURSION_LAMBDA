#1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:
def recVowelCount(s):
    if not s:
        return 0
    return (1 if s[0] in 'aeiouAEIOU' else 0) + recVowelCount(s[1:])

print(recVowelCount("I love python"))

"""
conter_2 = 0
def count_vou(word:str) ->int :
    conter_1=len(word)
    global conter_2
    if conter_1 == 0:
        return

    for i in word:
        if i == "a" or i == "A" or i == "e" or i == "E" or i == "o" or i == "O" or i == "u" or i == "U" or i == "i" or i == "I":
            conter_2 += 1
    print(conter_2)

count_vou("rahaf")
"""

## 2) Given a list of numbers : [40,35, 10, 15, 20]

#### create a new list containing each number from the previous list mutliplied by itself.
#### print the new list.
#### Hint: use map() with a lambda funciton

numbers = [40,35, 10, 15, 20]
numbers_2 = list(map(lambda element: element * element , numbers))

print(numbers_2)

