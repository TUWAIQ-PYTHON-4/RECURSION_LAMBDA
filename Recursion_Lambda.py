def VowelCount(s):
    vowels = "aeiouAEIOU"
    if s == "":
        return 0
    elif s[0] in vowels:
        return 1 + VowelCount(s[1:])
    else:
        return 0 + VowelCount(s[1:])

print(VowelCount("I love pythON"))

print("____________Q2_____________")
result=list(map(lambda n: n * n, [40, 35, 10, 15, 20]))
print(result)