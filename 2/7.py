def anagram(a, b):
    str1 = list(a.lower())
    str2 = list(b.lower())
    str1.sort()
    str2.sort()
    return str1 == str2
print(anagram('сосна', 'насос'))
print(anagram('напалм', 'баян'))