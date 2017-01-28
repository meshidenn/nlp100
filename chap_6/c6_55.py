import re

class Info():
    def __init__(self,word,lemma,pos,ner):
        self.word = word
        self.lemma = lemma
        self.pos = pos
        self.ner = ner
    

def word_lem_pos(file):
    word = re.compile('<word>(.+)?</word>')
    lemma = re.compile('<lemma>(.+)?</lemma>')
    pos = re.compile('<POS>(.+)?</POS>')
    ner = re.compile('<NER>PERSON</NER>')
    token = re.compile('<token id=(.+)?>')
    infos = []
    for line in file:
        t = token.search(line)
        if t:
            wline = ''
            lline = ''
            Pline = ''
            nline = ''
        l = word.search(line)
        m = lemma.search(line)
        n = pos.search(line)
        o = ner.search(line)
        if l:
            wline1 = line.strip()
            wline2 = wline1.lstrip("\<word\>")
            wline = wline2.rstrip("\<\/word\>")
            print(wline)
#            words.append(wline)
        if m:
            lline1 = line.strip()
            lline2 = lline1.lstrip("\<lemmma\>")
            lline = lline2.rstrip("\<\/lemma\>")
            print(lline)
#            lemmas.append(lline)
        if n:
            Pline1 = line.strip()
            Pline2 = Pline1.lstrip("<POS>")
            Pline = Pline2.rstrip('</POS>')
            print(Pline,Pline2)
#            POSs.append(Pline)
        if o:
            nline1 = line.strip()
            nline2 = nline1.lstrip("<NER>")
            nline = nline2.rstrip("</NER>")
        if o:
            info = Info(wline,lline,Pline,nline)
            infos.append(info)

    return(infos)


def main():
    with open('nlp_sentence.txt.xml','r') as file:
      infos  = word_lem_pos(file)

    return(infos)

if __name__ == '__main__':
    infos = main()
    for i,info in enumerate(infos):
        if i == 0:
            with open('SCNLP_ProperN.txt','w') as f:
                print('{}\t{}\t{}\t{}'.format(info.word,info.lemma,info.pos,info.ner),file=f)
        else:
            with open('SCNLP_ProperN.txt','a') as f:
                print('{}\t{}\t{}\t{}'.format(info.word,info.lemma,info.pos,info.ner),file=f)
    

