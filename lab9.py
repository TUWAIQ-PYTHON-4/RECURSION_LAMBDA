def Count(s):
 vowels = "aeiouAEIOU"
 if s == "":
    return 0
 elif s[0] in vowels:
    return 1 + Count(s[1:])
 else:
    return 0 + Count(s[1:])

print(Count("I love python"))
numbers =  [40,35, 10, 15, 20]
list = list(map(lambda number : number*number, numbers))

print(list)