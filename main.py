
def word_phrase( word : str ):
    l_ph = word.lower()  

    vowels = "aeiou"   

    if l_ph ==  "" :
        return 0

    if l_ph[0] in vowels :
        return  1 + word_phrase(l_ph[1:])
    else :
      return 0 + word_phrase(l_ph[1:])

print(word_phrase( "I love python "))

print("--------------------")

list_num = [40,35, 10, 15, 20]

mul_numbers_list = list(map(lambda number : number * number , list_num))

print(mul_numbers_list)

