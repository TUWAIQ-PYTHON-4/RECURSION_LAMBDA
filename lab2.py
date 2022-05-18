#recursion, if given a word/phrase return how many vowels(a,e,i,o,u)
def isConsonant(ch):
	return ch.upper() in ['A', 'E', 'I', 'O', 'U']


def totalConsonants(string, n):
	
	if n == 1:
		return isConsonant(string[0])

	return totalConsonants(string, n - 1) + isConsonant(string[n-1])


string = "I love python"
print(totalConsonants(string, len(string)))

#Q2
old_list = [40,35, 10, 15, 20]

new_list = old_list
print("new list",new_list)
result = list(map(lambda x, y: x * y, old_list, new_list))
print(result)