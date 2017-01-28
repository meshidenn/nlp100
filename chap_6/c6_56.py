import re

class Coreference():
    def __init__(self,sentence,start,end,head,text,rep):
        self.sentence = sentence
        self.start = start
        self.end = end
        self.head = head
        self.text = text
        self.rep = rep
    

def replace_m2rep(file):
    sentence = re.compile('<sentence>(.+)?</sentence>')
    start = re.compile('<start>(.+)?</start>')
    end = re.compile('<end>(.+)?</end>')
    head = re.compile('<head>(.+)?</head>')
    text = re.compile('<text>(.+)?</text>')
    ment = re.compile('<mention')
    repre = re.compile('representative\\=\\"true\\"')
    infos = []
    rep = ''
    for line in file:
        t = ment.search(line)
        r = repre.search(line)
        if t:
            seline = ''
            stline = ''
            eline = ''
            hline = ''
            tline = ''
            sw = 0
        if r:
            sw = 1
            rep = ''
            continue
        l = sentence.search(line)
        m = start.search(line)
        n = end.search(line)
        o = head.search(line)
        p = text.search(line)
        if l:
            seline1 = line.strip()
            seline2 = seline1.lstrip("\\<sentence\\>")
            seline = seline2.rstrip("\\<\\/sentence\\>")
            print(seline)
#            words.append(wline)
        if m:
            stline1 = line.strip()
            stline2 = stline1.lstrip("\\<start\\>")
            stline = stline2.rstrip("\\<\\/start\\>")
            print(stline)
#            lemmas.append(lline)
        if n:
            eline1 = line.strip()
            eline2 = eline1.lstrip("\\<end\\>")
            eline = eline2.rstrip('\\<\\/end\\>')
            print(eline)
#            POSs.append(Pline)
        if o:
            hline1 = line.strip()
            hline2 = hline1.lstrip("\\<head\\>")
            hline = hline2.rstrip("\\<\\/head\\>")
            print(hline)
        if p:
            tline1 = line.strip()
            tline2 = tline1.lstrip("\\<text\\>")
            tline = tline2.rstrip("\\<\\/text\\>")
            if sw:
                rep = tline
                print(tline)
        if p:
            info = Coreference(int(seline),int(stline),int(eline),int(hline),tline,rep)
            infos.append(info)

    return(infos)


def main():
    with open('nlp_sentence.txt.xml','r') as file:
      infos  = replace_m2rep(file)

#    sinfos = sorted(infos, key=lambda x: x[0])

    return(infos)

if __name__ == '__main__':
    infos = main()
    print(infos)
    with open('nlp_sentence.txt','r') as sentencefile:
        for i,line in enumerate(sentencefile):
            n = 0
            replace = []
            lsentence = []
            sentence = ''
            words = line.split(' ')
            for j,info in enumerate(infos):
                words = line.split(' ')
#                print(i,info.sentence)
                if i == info.sentence:
                    insert = '<ref>' + info.rep + '</ref>'
                    print(insert)
                    replace.append([info.start,info.end,insert])
                    continue
                else:
                    continue
#            print('r',replace)    
            replace.sort(key=lambda x:x[0])
            for k, word in enumerate(words):
                if len(replace) == 0:
                    lsentence.append(word)
                for rep in replace:
                    if k == rep[0]:
                        lsentence.append(rep[2])
                    elif rep[0] < k < rep[1]:
                        continue
                    elif rep == replace[-1]:
                        lsentence.append(word)

#            print('l',lsentence)        
            for w in lsentence:
                sentence += w + ' ' 
                        
            if i == 0:
                with open('Replace.txt','w') as f:
                    print(sentence,file=f)
                        
            else:
                with open('Replace.txt','a') as f:
                    print(sentence,file=f)
    
