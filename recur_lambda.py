## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

#### Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase . 
#### Example: given the phrase "I love python" , it should return : 4

list_vowls =['a','e','i','o','u']

def count_vowels(s:str) -> int:
    s = s.lower()
    if not any((c in list_vowls) for c in s):
        return 0
    return int(s[0] in list_vowls) + count_vowels(s[1:])

print(count_vowels('I love python'))

## 2) Given a list of numbers : [40,35, 10, 15, 20]

#### create a new list containing each number from the previous list mutliplied by itself.
#### print the new list.
#### Hint: use map() with a lambda funciton

num_list = [40,35, 10, 15, 20] 
final_list = list(map(lambda x: x*x, num_list))
print(final_list)
