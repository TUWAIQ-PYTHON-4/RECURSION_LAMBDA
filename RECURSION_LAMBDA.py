
## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

#### Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase . 
#### Example: given the phrase "I love python" , it should return : 4 

def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    if not word:
        return 0
    return int(word[0] in vowels) + count_vowels(word[1:])
print(count_vowels("NOURA"))

## 2) Given a list of numbers : [40,35, 10, 15, 20]

#### create a new list containing each number from the previous list mutliplied by itself.
#### print the new list.
#### Hint: use map() with a lambda funciton
numbers_list = [40, 35, 10, 15, 20]
lambda_list =list(map(lambda element : element*element ,numbers_list))
print(lambda_list)


