def isVowel(character): 
  character = character.lower() 

  vowels = "aeiou" 

  if character in vowels : 
    return 1
  else:
      return 0

def countVowels(string, n): 
	
  if n == 1 :
      return isVowel(string[0]) 
  else:

    return countVowels(string, n - 1) + isVowel(string[n - 1]) 

 
string = "I love python"
print(countVowels(string, len(string))) 



newlst=[40,35, 10, 15, 20]

filtered_numbers=list(map(lambda number:number*number,newlst))

print(filtered_numbers)