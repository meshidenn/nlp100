import re
import json
import requests
from collections import OrderedDict

f = open('jawiki-england.txt','r')
g = open('jawiki-england-basic-rmall.txt','w')

match = re.compile(r"^\|(.+?)=(.+)")
basic = OrderedDict()
begin = re.compile(r"\{\{基礎情報 国")
end = re.compile(r"\}\}")
inside_flg = False
prev_key = None
strong = re.compile(r"\'{1,3}(.+?)\'{1,3}")
inlink = re.compile(r"\[\[((.+?)\|)?(.+?)\]\]")
media = re.compile(r"[file|File|ファイル]:([\w\s\d]+\.[a-zA-Z\d]+)\|")
outlink = re.compile(r"\[(http://.+?)\]")
category = re.compile(r"\[\]Category:(.+?)\]\]")
redirect = re.compile(r"\#REDIRECT\[\[(.+?)\]\]")
note = re.compile(r"~~~~")
com = re.compile(r"\<!--(.+?)-->")

api = "http://ja.wikipedia.org/w/api.php?"

for line in f:
    if  begin.match(line):
        inside_flg = True
        continue
    
    if  end.match(line):
        inside_flg = False
        
    if inside_flg:
        m = re.search(match,line)
        if m:
            #key proc
            buf = strong.sub(r"\1",m.group(1))
            mid = inlink.sub(r"\3",buf)
            buf = media.sub(r"\1",mid)
            mid = outlink.sub(r"\1",buf)
            buf = category.sub(r"\1",mid)
            mid = redirect.sub(r"\1",buf)
            buf = note.sub(r"\1",mid)
            key = com.sub(r"\1",buf)
            #val proc            
            buf = strong.sub(r"\1",m.group(2))
            mid = inlink.sub(r"\3",buf)
            buf = media.sub(r"\1",mid)
            mid = outlink.sub(r"\1",buf)
            buf = category.sub(r"\1",mid)
            mid = redirect.sub(r"\1",buf)
            buf = note.sub(r"\1",mid)
            val = com.sub(r"\1",buf)
#print("key:%s,buf:%s,ch1:%s,ch2:%s,val:%s" % (key,buf,ch1,ch2,val))
            basic[key.strip()] = val.strip()
            prev_key = key.strip()
        else:
            buf = strong.sub(r"\1",line)
            mid = inlink.sub(r"\3",buf)
            buf = media.sub(r"\1",mid)
            mid = outlink.sub(r"\1",buf)
            buf = category.sub(r"\1",mid)
            mid = redirect.sub(r"\1",buf)
            buf = note.sub(r"\1",mid)
            val = com.sub(r"\1",buf)
            basic[prev_key] += val.strip()
          

#print(basic)
json.dump(basic,g,ensure_ascii=False)
template = json.dumps(basic,ensure_ascii=False)
print(template)

prop = {
    'action': "query",
    'prop': "imageinfo",
    'iiprop':"url",
    'format':"json",
}

for country in template:
    print(country)
    if '国旗画像' in country:
        print(country)
        filename = country['国旗画像']
        prop['titles'] = "Image:" + filename
        res = requests.get(url=api,params=prop)
        print(res)
        datum = json.loads(res.text, params=prop)
        try:
            file_url = datum['query']['pages'][0]['imageinfo'][0]['url']
        except:
            print(datum)
            break
        print(filename,file_url)
    


f.close()
g.close()
