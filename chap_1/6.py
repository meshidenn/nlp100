def ngram(char,n):
    gram = []
    l = len(char)
    for i in range(0,l-n+1):
        buf = ''
        for j in range(i,n+i):
            buf += char[j]
        gram.append(buf)

    return gram

c1 = 'paraparaparadise'
c2 = 'paragraph'

d1 = ngram(c1,2)
d2 = ngram(c2,2)

s1 = set(d1)
s2 = set(d2)

sadd = s1 | s2
sor = s1 & s2
smin = s1 - s2

a = 'se' in s1
b = 'se' in s2

print('s1:{0}'.format(s1))
print('s2:{0}'.format(s2))
print('sadd:{0}'.format(sadd))
print('sor:{0}'.format(sor))
print('smin:{0}'.format(smin))
print(a)
print(b)
