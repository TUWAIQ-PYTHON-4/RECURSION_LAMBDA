def isVowel(character): 
  character = character.lower() 

  vowels = "aeiou" 

  if character in vowels : 
    return 1
  else:
      return 0

def countVowels(string):
	count = 0
	for i in range(len(string)): 
		if isVowel(string[i]) :  
			count += 1
	return count 

 
string = "I love python"
print(countVowels(string)) 



newlst=[40,35, 10, 15, 20]

filtered_numbers=list(map(lambda number:number*number,newlst))

print(filtered_numbers)