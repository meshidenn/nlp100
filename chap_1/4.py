from collections import OrderedDict

s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine.\
 New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

dict = OrderedDict()
list = (0,4,5,6,7,8,14,15,18)

word = s.split()
lw = len(word)
ll = len(list)
j = 0

for i in range(0,lw):
    if i == list[j] & j <= ll:
        c = word[i][0]
        j += 1
    else:
        c = word[i][0] + word[i][1]
    dict[c]=i+1

print(dict)


