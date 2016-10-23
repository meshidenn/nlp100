import re

f = open('jawiki-england.txt','r')
g = open('jawiki-england-level-name.txt','w')

section = re.compile(r"=(=+)(.+)=\1")

for line in f:
    m = re.match(section, line)
    if m:
        level = int(line.count('=')/2 - 1)
#        name = re.sub("=",'', m.group(1))
        print('%s,level:%d' % (m.group(2),level))
        g.write('%s,level:%d\n' % (name,level))
        
f.close()
g.close()
