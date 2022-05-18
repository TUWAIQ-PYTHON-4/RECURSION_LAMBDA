
'''
## 1) Using recursion, if given a word/phrase 
# return how many vowels(a,e,i,o,u)
#  are in that phrase or word:
'''
def count_vowels(string: str= ' ', count = 0):
    ar = list(string)
    vowels = ['a','e','i','o','u']
    if not ar:
        return count

    if ar.pop().lower() in vowels:
        count += 1

    return count_vowels(''.join(ar), count)

string = 'i love python'
print(count_vowels(string))
    
'''
 2) Given a list of numbers : [40,35, 10, 15, 20] 
#### create a new list containing each number 
# from the previous list mutliplied by itself.
#### print the new list.
#### Hint: use map() with a lambda funciton
'''
int_list = [40,35, 10, 15, 20] 
print(list(map(lambda x: x*x, int_list)))

