## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) 
# are in that phrase or word:


def vowels(vowel): 
  return vowel.lower() in ['a','e','i','o','u']

input_u = "I love python"    
def check_vowels(input_u, n): 

  if n == 1 :
      return vowels(input_u[0]) 
  else:

    return check_vowels(input_u, n - 1) + vowels(input_u[n - 1]) 

print(check_vowels(input_u, len(input_u))) 


print("-"* 80)
## 2) Given a list of numbers : [40,35, 10, 15, 20]
nums = [40,35, 10, 15, 20]
print(nums)

new_list = nums
multiplying_nums = list(map(lambda x, y: x * y, nums, new_list))
print(multiplying_nums)

