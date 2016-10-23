import re
import json
from collections import OrderedDict

f = open('jawiki-england.txt','r')
g = open('jawiki-england-basic-rminlink.txt','w')

match = re.compile(r"^\|(.+)=(.+)")
basic = OrderedDict()
begin = re.compile(r"\{\{基礎情報 国")
end = re.compile(r"\}\}")
inside_flg = False
prev_key = None
strong = re.compile(r"\'{1,3}(.+?)\'{1,3}")
link = re.compile(r"\[\[(((.+?)\|)?(.+?)\]\]")

for line in f:
    if  begin.match(line):
        inside_flg = True
        continue
    
    if  end.match(line):
        inside_flg = False
        
    if inside_flg:
        m = re.search(match,line)
        if m:         
            buf = strong.sub(r"\1",m.group(1))
            key = link.sub(r"\3",buf)
            buf = strong.sub(r"\1",m.group(2))
            ch1 = link.sub(r"\1",buf)
            ch2 = link.sub(r"\4",buf)
            val = link.sub(r"\5",buf)
            print("key:%s,buf:%s,ch1:%s,ch2:%s,val:%s" % (key,buf,ch1,ch2,val))
            basic[key.strip()] = val.strip()
            prev_key = key.strip()
        else:
            basic[prev_key] += line.strip()
          

#print(basic)
json.dump(basic,g,ensure_ascii=False)
            
f.close()
g.close()
