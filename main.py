def Vowel(num):
    return num.upper() in ['A', 'E', 'I', 'O', 'U']
def VowelsCounter(str, n):
    if (n == 1):
        return Vowel(str[n - 1]);
    return (VowelsCounter(str, n - 1) + Vowel(str[n - 1]));
str = "I love python";
print(VowelsCounter(str, len(str)))




e_list = list(map(lambda element: element ** 2 ,[40,35, 10, 15, 20]))

print(e_list)