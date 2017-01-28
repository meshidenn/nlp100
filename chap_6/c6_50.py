import re

def sentencer(raw):
    sentences = []
    stock = ''
    for line in raw:
        if line != '\n':
            line.strip()
            lp = [-2]
            pattern = re.compile('[\\.\\?\\!\\;\\:]\\s[A-Z]')
            t = pattern.search(line)
            if t:
                sentence = []
                stock += line
                print(stock)
            else:
                stock += line.strip()+' '
                print(stock)
                continue
            liner  = pattern.finditer(stock)
            for pos in liner:
                lp.append(int(pos.start()))
            lp.append(len(stock))
            for i,pos in enumerate(lp[:-1]):
                print(i,stock[int(pos)+2:lp[i+1]+1].strip())
                sentence.append(stock[int(pos)+2:lp[i+1]+1].strip())
            if len(sentence) != 0 and pattern:           
                sentences.append(sentence)
                stock = ''

    return(sentences)

def main():
    with open('nlp.txt','r') as f:
        sentences = sentencer(f)

    return(sentences)

if __name__ == '__main__':
    sentences = main()
    for i,sentence in enumerate(sentences):
        for j,line in enumerate(sentence):
            if i == 0 and j == 0:
                with open('nlp_sentence.txt','w') as out:
                    print(line,file=out)
            else:
                with open('nlp_sentence.txt','a') as out:
                    print(line,file=out)
