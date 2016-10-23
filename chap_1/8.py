def cipher(char):
    c = ''
    l = len(char)
    if char.islower():
        for i in range(0,l):
            n = 219 - ord(char[i])
            c += chr(n)

        return c
    else:
        return char


s = 'cipher'
word = cipher(s)
print(word)

