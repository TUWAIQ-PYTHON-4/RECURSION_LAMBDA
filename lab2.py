#recursion, if given a word/phrase return how many vowels(a,e,i,o,u)
from itertools import count


def isVowel(ch):
	return ch.upper() in ['A', 'E', 'I', 'O', 'U']

def countVowel(str):
    count=0
    for i in range(len(str)):
        if isVowel(str[i]):
            count +=1
    return count 


str='I love python'
print(countVowel(str))

#Q2
old_list = [40,35, 10, 15, 20]

new_list = old_list
print("new list",new_list)
result = list(map(lambda x, y: x + y, old_list, new_list))
print(result)