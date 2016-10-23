import re

f = open('jawiki-england.txt','r')
g = open('jawiki-england-category-name.txt','w')

for line in f:
    if re.search('Category',line):
        proc = re.sub('\[\[Category:*','',line)
        proc2 = re.sub('\]\]','',proc)
        print(proc2, end = '')
        g.write(proc2)

f.close()
g.close()
