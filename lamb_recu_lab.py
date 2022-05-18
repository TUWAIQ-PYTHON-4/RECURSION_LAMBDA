def VowelCount(s):
    v=s.lower()
    if len(v) == 0:
        return 0
    letter = v[0]
    if letter in 'aeiou':
        return 1 + VowelCount(v[1:])
    return VowelCount(v[1:])

print(VowelCount('I Love Python'))

list1 = [40,35, 10, 15, 20]
multi = map(lambda x: x*x ,list1)
print(list(multi))
