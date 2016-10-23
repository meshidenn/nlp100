import re

f = open('jawiki-england.txt','r')
g = open('jawiki-england-media.txt','w')

media = re.compile(r"[file|File|ファイル]:([\w\s\d]+\.[a-zA-Z\d]+)\|")

for line in f:
    m = re.search(media,line)
    if m:
        print(m.group(1))
        g.write(m.group(1)+'\n')

f.close()
g.close()
