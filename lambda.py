"""
letter={"a","e","o","i","u"}

def letters (inpur_word:str):
    global letter
    inpur_word={}
    if len(inpur_word) == len(letter):
     return len(letter)
        

letters("ahmed")

def Check_Vow(string):
    vowels= {"a","e","o","i","u"}
    final = [each for each in string if each in vowels]
    print(len(final))
    

Check_Vow("ahmed")"""
numbers =[40,35, 10, 15, 20]

nmumbermulti = list(map(lambda number : number*number,numbers))

print(nmumbermulti)