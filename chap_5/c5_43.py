import c5_40 as p40
import c5_41 as p41

def parse(sentences):
    phrases = []
    n = len(sentences)
    for i in range(n):
        phrase = []
        for j, chunk in enumerate(sentences[i]):
            pos = []
            surfaces = ""
            for morph in chunk.morphs:
                surfaces += morph.surface
                if morph.pos != '記号':
                    pos.append(morph.pos)
            phrase.append((j,surfaces,pos,chunk.dst))
        phrases.append(phrase)

    return phrases

def main():
    with open('neko.txt.cabocha','r') as cabochafile:
        sentences = p41.chunk_reader(cabochafile)

    phrases = parse(sentences)

    return phrases

if __name__ == '__main__':
    phrases = main()    
    n = len(phrases)
    for i, phrase in enumerate(phrases):
        nn = len(phrase)
        for j in range(nn):
            if int(phrase[j][3]) == -1:
                k = 0
            else:
                k = int(phrase[j][3])
            if '名詞' in phrase[j][2] and '動詞' in phrase[k][2]:
                print(phrase[j][1].strip('、。　'), '\t', phrase[k][1].strip('、。　'))
