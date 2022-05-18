from unittest import result


def vowels_count(phrase:str):
    lower_phrase=phrase.lower()
    v_letters="aeiou"

    if lower_phrase=="":
        return 0
    if lower_phrase[0] in v_letters:
        return 1+ vowels_count(lower_phrase[1:])
    else:    
      return 0 + vowels_count(lower_phrase[1:])

print(vowels_count("I love python"))


#####################################################
num = [40,35, 10, 15, 20]
result=map(lambda n:n*n,num)
print(list(result))

