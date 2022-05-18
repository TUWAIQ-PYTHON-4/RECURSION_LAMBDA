'''
1) Using recursion,
if given a word/phrase return how many vowels(a,e,i,o,u)
are in that phrase or word:
'''

# define function
def vowels_count(phrase: str):
    # lowercase all letters of the phrase
    lower_phrase= phrase.lower()
    v_letters= "aeiou"
    # empty string
    if lower_phrase =="":
        return 0
    # check if vowel letter exists in phrase
    if lower_phrase[0] in v_letters:
        return 1 + vowels_count(lower_phrase[1:]) # it keeps adding one and slicing the previous letter
    return vowels_count(lower_phrase[1:]) # if other characters/letters (not vowel), it keeps slicing the string (ignore)

print(vowels_count("I love python"))

'''
 2) Given a list of numbers : [40,35, 10, 15, 20]

create a new list containing each number from the previous 
list mutliplied by itself.

print the new list.

Hint: use map() with a lambda funciton
'''
lst_num= [40,35, 10, 15, 20]

new_lst = list(map(lambda num:num*num,lst_num))

print(new_lst)
