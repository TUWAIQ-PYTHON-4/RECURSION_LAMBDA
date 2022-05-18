def VowelCount(s):
    v=s.lower()
    if len(v) == 0:
        return 0
    letter = v[0]
    if letter in 'aeiou':
        return 1 + VowelCount(v[1:])
    return VowelCount(v[1:])

print(VowelCount('I Love Python'))

list_1 = [40,35, 10, 15, 20]
cubed = map(lambda x: x*x ,list_1)
print(list(cubed))
