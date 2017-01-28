import re

class Info():
    def __init__(self,word,lemma,pos):
        self.word = word
        self.lemma = lemma
        self.pos = pos
    

def word_lem_pos(file):
    word = re.compile('<word>(.+)?</word>')
    lemma = re.compile('<lemma>(.+)?</lemma>')
    pos = re.compile('<POS>(.+)?</POS>')
    token = re.compile('<token id=(.+)?>')
    infos = []
    for line in file:
        t = token.search(line)
        if t:
            wline = ''
            lline = ''
            Pline = ''
        l = word.search(line)
        m = lemma.search(line)
        n = pos.search(line)
        if l:
            wline1 = line.strip()
            wline2 = wline1.strip("<word>")
            wline = wline2.strip("</word>")
            print(wline)
#            words.append(wline)
        if m:
            lline1 = line.strip()
            lline2 = lline1.strip("<lemmma>")
            lline = lline2.strip("</lemma>")
            print(lline)
#            lemmas.append(lline)
        if n:
            Pline1 = line.strip()
            Pline2 = Pline1.strip(r"<POS>")
            Pline = Pline2.strip("</POS>")
            print(Pline)
#            POSs.append(Pline)
        if n:
            info = Info(wline,lline,Pline)
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
            with open('SCNLP_tag.txt','w') as f:
                print('{}\t{}\t{}'.format(info.word,info.lemma,info.pos),file=f)
        else:
            with open('SCNLP_tag.txt','a') as f:
                print('{}\t{}\t{}'.format(info.word,info.lemma,info.pos),file=f)
    

