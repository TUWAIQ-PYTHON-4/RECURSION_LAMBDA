

def vowels_count(string: str):
    if not string:
        return 0
    return (1 if string[0] in 'aeiouAEIOU' else 0) + vowels_count(string[1:])
   
   
print(vowels_count('I love python'))



numbers = [40,35, 10, 15, 20]

multi_list= list(map(lambda result: result * result , numbers))

print(multi_list)


