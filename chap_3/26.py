import re
import json
from collections import OrderedDict

f = open('jawiki-england.txt','r')
g = open('jawiki-england-basic-rmst.txt','w')

match = re.compile(r"^\|(.+)=(.+)")
basic = OrderedDict()
begin = re.compile(r"\{\{基礎情報 国")
end = re.compile(r"\}\}")
inside_flg = False
prev_key = None
lstrong = re.compile(r"\"{1,3}")
rstrong = re.compile(r"\"{1,3}")


for line in f:
    if  begin.match(line):
        inside_flg = True
        continue
    
    if  end.match(line):
        inside_flg = False
        
    if inside_flg:
        m = re.search(match,line)
        if m:         
            buf = re.sub(lstrong,'',m.group(1))
            key = re.sub(rstrong,'',buf)         
            buf = re.sub(lstrong,'',m.group(2))
            val = re.sub(rstrong,'',buf)       
            basic[key.strip()] = val.strip()
            prev_key = key.strip()
        else:
            basic[prev_key] += line.strip()
          

print(basic)
json.dump(basic,g,ensure_ascii=False)
            
f.close()
g.close()
