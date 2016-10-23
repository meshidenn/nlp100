import re
import json
from collections import OrderedDict

f = open('jawiki-england.txt','r')
g = open('jawiki-england-basic.txt','w')

match = re.compile(r"^\|(.+)=(.+)")
basic = OrderedDict()
begin = re.compile(r"\{\{基礎情報 国")
end = re.compile(r"\}\}")
inside_flg = False
prev_key = None

for line in f:
    if  begin.match(line):
        inside_flg = True
        continue
    
    if  end.match(line):
        inside_flg = False
        
    if inside_flg:
        m = re.search(match,line)
        if m:
            basic[m.group(1).strip()] = m.group(2).strip()
            prev_key = m.group(1).strip()
        else:
#            m2 = re.search(r"(.*)\}\}", line)
#            if m2:
#                basic[prev_key] += m2.group(1).strip()
#                inside_flg = False
#            else:
            basic[prev_key] += line.strip()
          

#for i in basic:
#    print('項目:%s,値:%s' %(i,basic[i]))
#    g.write('項目:%s,値:%s\n' %(i,basic[i]))

print(basic)
json.dump(basic,g,ensure_ascii=False)

f.close()
g.close()
