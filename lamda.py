#Q1
count = 0
max = 0

def vowels(word):
    global max, count
    word = word.lower()
    if word[max] == 'a' or word[max] == 'i' or word[max] == 'e' or word[max] == 'o' or word[max] == 'u' :
        count = count + 1

    max = max + 1
    if max == len(word):
        return count
    else:
        return vowels(word)


word = "I love python"

print(vowels(word))
 #Q2
number = [1,2,3]
output = list(map(lambda x: x*x, number))

print(output)