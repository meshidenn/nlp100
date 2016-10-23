import random

s = "I couldn't believe that I could actually understand what I was reading:\
    the phenomenal power of the human mind."
l = len(s)
buf = []
for i in range(1,l-1):
    buf.append(s[i])

random.shuffle(buf)

print(buf)

typo = ''
typo += s[0]
for i in range(0,l-2):
    typo += buf[i]

typo += s[l-1]
    
print(typo)
