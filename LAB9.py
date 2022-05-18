# 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:
def vowels_recursion(word: str):
    
    upper_word= word.upper()
    vowels_letters= "AEIOU"
    
    # check if the word is empty
    if upper_word =="":
        return 0

    elif upper_word[0] in vowels_letters:
        return 1 + vowels_recursion(upper_word[1:])
        
    else:     
        return vowels_recursion(upper_word[1:]) 

print(vowels_recursion("I love python"))      


# 2) Given a list of numbers : [40,35, 10, 15, 20]
my_list = [40, 35, 10, 15, 20]

 # create a new list containing each number from the previous list mutliplied by itself.
new_list = map(lambda element: element*element, my_list)
print(list(new_list))