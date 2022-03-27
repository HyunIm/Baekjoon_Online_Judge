word = input()
vowels = ['a', 'e', 'i', 'o', 'u']
result = 0

for vowel in vowels:
    result += word.count(vowel)
print(result)
