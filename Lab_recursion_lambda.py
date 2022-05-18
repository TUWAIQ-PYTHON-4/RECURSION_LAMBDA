# RECURSION_LAMBDA


## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

#### Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase . 
#### Example: given the phrase "I love python" , it should return : 4 

from xxlimited import new


def check_vowels(word):
    '''
        The check_vowels function counts the vowels and return the final 
        count - in recursion
    '''
    if not word:
        return 0
    if word[0] not in "AaOoIiEeUu":
        counter = 0 
    else:
        counter = 1 
    return counter + check_vowels(word[1:])

print(check_vowels('I Love Python'))


## 2) Given a list of numbers : [40,35, 10, 15, 20]

#### create a new list containing each number from the previous list mutliplied by itself.
#### print the new list.
#### Hint: use map() with a lambda funciton

numbers_list = [40,35, 10, 15, 20]

new_numbers_list = map(lambda x: x*x , numbers_list)

print(list(new_numbers_list))