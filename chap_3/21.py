import re

f = open('jawiki-england.txt','r')
g = open('jawiki-england-category.txt','w')

for line in f:
    if re.search('Category',line):
        print(line, end = '')
        g.write(line)

f.close()
g.close()
