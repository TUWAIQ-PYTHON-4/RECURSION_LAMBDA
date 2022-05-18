
from calendar import c


def isVowel(character): 
   characters = character.lower() 

   vowels = "aeiou" 
   if characters =="":
       return 0
   if characters[0] in vowels : 
     return 1+isVowel(characters[1:])
    
   else:
       return 0 +isVowel(characters[1:])
   

print(isVowel("I love python")) 
#second code

newlst=[40,35, 10, 15, 20]

filtered_numbers=list(map(lambda number:number*number,newlst))

print(filtered_numbers)